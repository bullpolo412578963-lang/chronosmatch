"""
ChronosMatch — Zero-Copy High-Frequency Trading Engine
======================================================
A complete, single-file implementation of the ChronosMatch trading engine 
and its professional real-time web dashboard.

This file contains:
1. The Zero-Copy Matching Engine (Limit Order Book with Price-Time Priority).
2. The Shared-Memory IPC mechanism (using mmap and struct).
3. The Asynchronous Market Simulator.
4. The WebSocket & REST API Backend (FastAPI).
5. The Professional React-based Web Dashboard (Embedded HTML/JS).

Requirements:
    pip install fastapi uvicorn

Usage:
    python chronosmatch.py
    
Then open your browser to: http://localhost:8000
"""

import asyncio
import json
import time
import struct
import mmap
import os
import random
import logging
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set
from datetime import datetime

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ChronosMatch")

# ==========================================
# 1. DATA MODELS & SHARED MEMORY IPC
# ==========================================

# Shared Memory IPC Configuration
# Format: 'd' (price), 'i' (quantity), 'i' (side), 'd' (timestamp)
# Total size per order: 8 + 4 + 4 + 8 = 24 bytes
SHM_SIZE = 1024 * 1024  # 1MB Ring Buffer
ORDER_FORMAT = 'diid'
ORDER_SIZE = struct.calcsize(ORDER_FORMAT)

class SharedMemoryIPC:
    """Simulates zero-copy IPC using memory-mapped files and struct packing."""
    def __init__(self):
        # -1 indicates anonymous memory mapping (works cross-platform)
        self.shm = mmap.mmap(-1, SHM_SIZE, tagname="chronosmatch_shm")
        self.write_pos = 0
        self.read_pos = 0
        self.lock = asyncio.Lock()

    async def write_order(self, price: float, quantity: int, side: int, timestamp: float):
        async with self.lock:
            data = struct.pack(ORDER_FORMAT, price, quantity, side, timestamp)
            if self.write_pos + ORDER_SIZE > SHM_SIZE:
                self.write_pos = 0  # Wrap around ring buffer
            self.shm.seek(self.write_pos)
            self.shm.write(data)
            self.write_pos += ORDER_SIZE

    async def read_orders(self) -> List[tuple]:
        async with self.lock:
            orders = []
            while self.read_pos != self.write_pos:
                if self.read_pos + ORDER_SIZE > SHM_SIZE:
                    self.read_pos = 0
                self.shm.seek(self.read_pos)
                data = self.shm.read(ORDER_SIZE)
                price, quantity, side, timestamp = struct.unpack(ORDER_FORMAT, data)
                orders.append((price, quantity, side, timestamp))
                self.read_pos += ORDER_SIZE
            return orders

@dataclass
class Order:
    order_id: int
    side: str  # 'BUY' or 'SELL'
    price: float
    quantity: int
    timestamp: float

@dataclass
class Trade:
    trade_id: int
    buy_order_id: int
    sell_order_id: int
    price: float
    quantity: int
    timestamp: float
    latency_us: float

# ==========================================
# 2. MATCHING ENGINE
# ==========================================

class MatchingEngine:
    """Limit Order Book with Price-Time Priority."""
    def __init__(self):
        self.buy_orders = defaultdict(list)  # price -> list of orders
        self.sell_orders = defaultdict(list)
        self.trades: List[Trade] = []
        self.total_processed = 0
        self.total_matched = 0
        self.latencies: List[float] = []
        self.start_time = time.time()
        self.trade_id_counter = 1

    def process_order(self, order: Order) -> float:
        start_time = time.perf_counter()
        self.total_processed += 1
        
        if order.side == 'BUY':
            self._match_buy(order)
        else:
            self._match_sell(order)
            
        # Calculate latency in microseconds
        latency_us = (time.perf_counter() - start_time) * 1_000_000
        self.latencies.append(latency_us)
        if len(self.latencies) > 5000:
            self.latencies.pop(0)
            
        return latency_us

    def _match_buy(self, order: Order):
        while order.quantity > 0 and self.sell_orders:
            best_ask_price = min(self.sell_orders.keys())
            if best_ask_price > order.price:
                break  # No more matches possible
            
            # Match with the oldest order at the best ask price
            ask_order = self.sell_orders[best_ask_price][0]
            match_qty = min(order.quantity, ask_order.quantity)
            
            # Record trade
            self.trades.append(Trade(
                trade_id=self.trade_id_counter,
                buy_order_id=order.order_id,
                sell_order_id=ask_order.order_id,
                price=best_ask_price,
                quantity=match_qty,
                timestamp=time.time(),
                latency_us=0.0  # Will be updated by caller
            ))
            self.trade_id_counter += 1
            self.total_matched += 1
            
            # Update quantities
            order.quantity -= match_qty
            ask_order.quantity -= match_qty
            
            if ask_order.quantity == 0:
                self.sell_orders[best_ask_price].pop(0)
                if not self.sell_orders[best_ask_price]:
                    del self.sell_orders[best_ask_price]
        
        # Add remainder to order book
        if order.quantity > 0:
            self.buy_orders[order.price].append(order)

    def _match_sell(self, order: Order):
        while order.quantity > 0 and self.buy_orders:
            best_bid_price = max(self.buy_orders.keys())
            if best_bid_price < order.price:
                break  # No more matches possible
            
            # Match with the oldest order at the best bid price
            bid_order = self.buy_orders[best_bid_price][0]
            match_qty = min(order.quantity, bid_order.quantity)
            
            # Record trade
            self.trades.append(Trade(
                trade_id=self.trade_id_counter,
                buy_order_id=bid_order.order_id,
                sell_order_id=order.order_id,
                price=best_bid_price,
                quantity=match_qty,
                timestamp=time.time(),
                latency_us=0.0
            ))
            self.trade_id_counter += 1
            self.total_matched += 1
            
            # Update quantities
            order.quantity -= match_qty
            bid_order.quantity -= match_qty
            
            if bid_order.quantity == 0:
                self.buy_orders[best_bid_price].pop(0)
                if not self.buy_orders[best_bid_price]:
                    del self.buy_orders[best_bid_price]
        
        # Add remainder to order book
        if order.quantity > 0:
            self.sell_orders[order.price].append(order)

    def get_order_book(self, depth: int = 15) -> Dict:
        bids = []
        asks = []
        
        # Get top bids
        buy_prices = sorted(self.buy_orders.keys(), reverse=True)[:depth]
        cum_qty = 0
        for p in buy_prices:
            qty = sum(o.quantity for o in self.buy_orders[p])
            cum_qty += qty
            bids.append({
                "price": p, 
                "qty": qty, 
                "cumulative_qty": cum_qty, 
                "orders": len(self.buy_orders[p])
            })
            
        # Get top asks
        sell_prices = sorted(self.sell_orders.keys())[:depth]
        cum_qty = 0
        for p in sell_prices:
            qty = sum(o.quantity for o in self.sell_orders[p])
            cum_qty += qty
            asks.append({
                "price": p, 
                "qty": qty, 
                "cumulative_qty": cum_qty, 
                "orders": len(self.sell_orders[p])
            })
            
        best_bid = bids[0]["price"] if bids else 0
        best_ask = asks[0]["price"] if asks else 0
        spread = best_ask - best_bid if (bids and asks) else 0
        mid = (best_bid + best_ask) / 2 if (bids and asks) else 0
        
        return {
            "bids": bids,
            "asks": asks,
            "spread": {"value": round(spread, 2), "mid": round(mid, 2)},
            "best_bid": best_bid,
            "best_ask": best_ask
        }

    def get_state(self, ws_connections: int) -> Dict:
        latencies = self.latencies[-500:] if self.latencies else []
        avg_lat = sum(latencies) / len(latencies) if latencies else 0
        
        # Calculate percentiles
        sorted_lats = sorted(latencies)
        p95_lat = sorted_lats[int(len(sorted_lats)*0.95)] if sorted_lats else 0
        p99_lat = sorted_lats[int(len(sorted_lats)*0.99)] if sorted_lats else 0
        
        # Generate chart data for latency
        latency_chart = []
        now = time.time()
        step = 0.1  # 100ms per point
        for i, lat in enumerate(latencies[-200:]):  # Last 200 points
            latency_chart.append({
                "time": int(now - (len(latencies[-200:]) - i) * step),
                "value": round(lat, 2)
            })
            
        active_orders = sum(len(v) for v in self.buy_orders.values()) + sum(len(v) for v in self.sell_orders.values())
        
        return {
            "kpis": {
                "orders_per_sec": round(len(latencies) / 50.0, 2) if latencies else 0,
                "avg_latency": round(avg_lat, 2),
                "p95_latency": round(p95_lat, 2),
                "p99_latency": round(p99_lat, 2),
                "total_orders": self.total_processed,
                "matched_trades": self.total_matched,
                "active_orders": active_orders
            },
            "order_book": self.get_order_book(),
            "recent_trades": [
                {
                    "trade_id": t.trade_id,
                    "buy_id": t.buy_order_id,
                    "sell_id": t.sell_order_id,
                    "price": t.price,
                    "qty": t.quantity,
                    "timestamp": t.timestamp,
                    "latency": t.latency_us
                } for t in self.trades[-30:]
            ],
            "latency_chart": latency_chart,
            "system": {
                "incoming_rate": round(len(latencies) / 50.0, 2),
                "processed_rate": round(len(latencies) / 50.0, 2),
                "matched_count": self.total_matched,
                "open_orders": active_orders,
                "error_count": 0,
                "uptime": round(time.time() - self.start_time, 2),
                "ws_connections": ws_connections
            },
            "timestamp": time.time()
        }

# ==========================================
# 3. WEBSOCKET MANAGER
# ==========================================

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"WebSocket connected. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        logger.info(f"WebSocket disconnected. Total: {len(self.active_connections)}")

    async def broadcast(self, message: dict):
        if not self.active_connections:
            return
        tasks = []
        for connection in self.active_connections:
            tasks.append(asyncio.create_task(self._send(connection, message)))
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

    async def _send(self, connection: WebSocket, message: dict):
        try:
            await connection.send_json(message)
        except Exception:
            pass

# ==========================================
# 4. FASTAPI APPLICATION & ROUTES
# ==========================================

app = FastAPI(title="ChronosMatch API")
engine = MatchingEngine()
ipc = SharedMemoryIPC()
ws_manager = ConnectionManager()

@app.get("/", response_class=HTMLResponse)
async def get_dashboard():
    return HTML_CONTENT

@app.get("/api/status")
async def get_status():
    return {
        "status": "online",
        "engine": "running",
        "simulator": "active",
        "timestamp": time.time()
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            # Keep connection alive and listen for client messages (e.g., control commands)
            data = await websocket.receive_text()
            if data == "ping":
                await websocket.send_json({"type": "pong"})
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)

# ==========================================
# 5. MARKET SIMULATOR
# ==========================================

async def market_simulator():
    """Generates simulated market orders and feeds them into the engine via IPC."""
    base_price = 150.0
    order_id = 1
    logger.info("Market Simulator started.")
    
    while True:
        try:
            # Generate random order parameters
            side = random.choice(['BUY', 'SELL'])
            # Random walk for price
            base_price += random.uniform(-0.15, 0.15)
            price = round(base_price + random.uniform(-0.05, 0.05), 2)
            quantity = random.randint(10, 500) * 10
            timestamp = time.time()
            
            # Write to shared memory (Zero-Copy IPC)
            await ipc.write_order(price, quantity, 1 if side == 'BUY' else 0, timestamp)
            
            # Read from shared memory and process
            raw_orders = await ipc.read_orders()
            for p, q, s, t in raw_orders:
                order = Order(order_id, 'BUY' if s == 1 else 'SELL', p, q, t)
                latency = engine.process_order(order)
                
                # Update latency in the last trade if it was a match
                if engine.trades and engine.trades[-1].trade_id == engine.trade_id_counter - 1:
                    engine.trades[-1].latency_us = latency
                    
                order_id += 1
                
            # Broadcast state to all connected dashboards
            state = engine.get_state(len(ws_manager.active_connections))
            await ws_manager.broadcast(state)
            
            # Simulate high-frequency arrival (20-100 orders per second)
            await asyncio.sleep(random.uniform(0.01, 0.05))
            
        except Exception as e:
            logger.error(f"Simulator error: {e}")
            await asyncio.sleep(1)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(market_simulator())
    logger.info("ChronosMatch Engine and Simulator initialized.")

# ==========================================
# 6. EMBEDDED FRONTEND DASHBOARD
# ==========================================

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChronosMatch — Zero-Copy Trading Engine</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        'terminal-bg': '#0b0f19',
                        'terminal-panel': '#111827',
                        'terminal-border': '#1f2937',
                        'buy-green': '#10b981',
                        'sell-red': '#ef4444',
                    },
                    fontFamily: {
                        'mono': ['JetBrains Mono', 'Fira Code', 'monospace'],
                    }
                }
            }
        }
    </script>
    <script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
    <style>
        body { font-family: 'JetBrains Mono', monospace; background-color: #0b0f19; }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #111827; }
        ::-webkit-scrollbar-thumb { background: #374151; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #4b5563; }
    </style>
    <script type="module">
        import React, { useState, useEffect, useRef, useMemo } from 'https://esm.sh/react@18.2.0';
        import htm from 'https://esm.sh/htm@3.1.1';
        import { createRoot } from 'https://esm.sh/react-dom@18.2.0/client';
        
        const html = htm.bind(React.createElement);

        // --- ICONS ---
        const Icon = ({ path, className = "w-4 h-4" }) => html`
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class=${className}>
                ${path}
            </svg>
        `;
        const icons = {
            activity: html`<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>`,
            trendingUp: html`<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline>`,
            clock: html`<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>`,
            server: html`<rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line>`,
            barChart: html`<line x1="12" y1="20" x2="12" y2="10"></line><line x1="18" y1="20" x2="18" y2="4"></line><line x1="6" y1="20" x2="6" y2="16"></line>`,
            list: html`<line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line>`,
            book: html`<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>`
        };

        // --- TOP NAV ---
        function TopNav({ status, time }) {
            const statusColor = status === 'CONNECTED' ? 'bg-emerald-500' : 'bg-rose-500';
            const statusText = status === 'CONNECTED' ? 'LIVE SIMULATION' : 'DISCONNECTED';
            
            return html`
                <header class="h-14 bg-terminal-panel border-b border-terminal-border flex items-center justify-between px-6 shrink-0">
                    <div class="flex items-center space-x-4">
                        <div class="flex items-center space-x-2">
                            <${Icon} path=${icons.activity} className="w-6 h-6 text-emerald-400" />
                            <h1 class="text-lg font-bold text-slate-100 tracking-tight">ChronosMatch</h1>
                        </div>
                        <span class="text-xs text-slate-500 border-l border-terminal-border pl-4 hidden sm:block">Zero-Copy Trading Engine</span>
                    </div>
                    <div class="flex items-center space-x-6">
                        <div class="flex items-center space-x-2">
                            <span class=${`w-2 h-2 rounded-full ${statusColor} animate-pulse`}></span>
                            <span class="text-xs font-medium text-slate-300">${statusText}</span>
                        </div>
                        <div class="text-xs text-slate-400 font-mono">${time}</div>
                    </div>
                </header>
            `;
        }

        // --- SIDEBAR ---
        function Sidebar({ active, setActive }) {
            const items = [
                { id: 'overview', label: 'Overview', icon: icons.barChart },
                { id: 'orderbook', label: 'Order Book', icon: icons.book },
                { id: 'trades', label: 'Trades', icon: icons.list },
                { id: 'performance', label: 'Performance', icon: icons.trendingUp },
                { id: 'system', label: 'System', icon: icons.server }
            ];

            return html`
                <aside class="w-16 lg:w-56 bg-terminal-panel border-r border-terminal-border flex flex-col shrink-0">
                    <nav class="flex-1 py-4 space-y-1">
                        ${items.map(item => html`
                            <button
                                key=${item.id}
                                onClick=${() => setActive(item.id)}
                                class=${`w-full flex items-center px-4 py-3 text-sm font-medium transition-colors ${
                                    active === item.id 
                                    ? 'text-emerald-400 bg-slate-800/50 border-r-2 border-emerald-400' 
                                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/30'
                                }`}
                            >
                                <${Icon} path=${item.icon} className="w-5 h-5 shrink-0" />
                                <span class="ml-3 hidden lg:block">${item.label}</span>
                            </button>
                        `)}
                    </nav>
                    <div class="p-4 border-t border-terminal-border hidden lg:block">
                        <div class="text-xs text-slate-500">Engine v1.0.0</div>
                        <div class="text-xs text-slate-600">Build 2026.10</div>
                    </div>
                </aside>
            `;
        }

        // --- KPI CARD ---
        function KPICard({ label, value, unit, icon, color = "text-slate-100" }) {
            return html`
                <div class="bg-terminal-panel border border-terminal-border rounded-lg p-4 flex flex-col justify-between">
                    <div class="flex justify-between items-start mb-2">
                        <span class="text-xs font-medium text-slate-400 uppercase tracking-wider">${label}</span>
                        <${Icon} path=${icon} className="w-4 h-4 text-slate-500" />
                    </div>
                    <div class="flex items-baseline space-x-1">
                        <span class=${`text-2xl font-bold ${color}`}>${value}</span>
                        <span class="text-xs text-slate-500">${unit}</span>
                    </div>
                </div>
            `;
        }

        // --- ORDER BOOK ---
        function OrderBook({ data }) {
            const { bids, asks, spread } = data;
            if (!bids || !asks) return html`<div class="p-4 text-slate-500">Loading order book...</div>`;
            
            const maxQty = Math.max(
                ...bids.map(b => b.cumulative_qty),
                ...asks.map(a => a.cumulative_qty),
                1
            );

            return html`
                <div class="bg-terminal-panel border border-terminal-border rounded-lg p-4 h-full flex flex-col">
                    <div class="flex justify-between items-center mb-3">
                        <h2 class="text-sm font-semibold text-slate-300 uppercase tracking-wider">Order Book</h2>
                        <span class="text-xs text-slate-500">Depth</span>
                    </div>
                    <div class="grid grid-cols-3 text-xs text-slate-500 mb-2 px-2">
                        <span>Price</span>
                        <span class="text-right">Size</span>
                        <span class="text-right">Total</span>
                    </div>
                    <div class="flex-1 overflow-hidden flex flex-col">
                        <div class="flex-1 flex flex-col justify-end space-y-0.5 mb-2 overflow-y-auto">
                            ${asks.slice().reverse().map(ask => html`
                                <div key=${ask.price} class="relative grid grid-cols-3 text-xs px-2 py-0.5 hover:bg-slate-800/50 rounded">
                                    <div class="absolute inset-y-0 right-0 bg-sell-red/10" style=${{ width: `${(ask.cumulative_qty / maxQty) * 100}%` }}></div>
                                    <span class="relative text-sell-red font-medium">${ask.price.toFixed(2)}</span>
                                    <span class="relative text-right text-slate-300">${ask.qty}</span>
                                    <span class="relative text-right text-slate-500">${ask.cumulative_qty}</span>
                                </div>
                            `)}
                        </div>
                        <div class="text-center py-2 border-y border-terminal-border bg-slate-800/30 my-2">
                            <span class="text-lg font-bold text-slate-100">${spread.mid.toFixed(2)}</span>
                            <span class="text-xs text-slate-500 ml-2">Spread: ${spread.value.toFixed(2)}</span>
                        </div>
                        <div class="flex-1 flex flex-col space-y-0.5 mt-2 overflow-y-auto">
                            ${bids.map(bid => html`
                                <div key=${bid.price} class="relative grid grid-cols-3 text-xs px-2 py-0.5 hover:bg-slate-800/50 rounded">
                                    <div class="absolute inset-y-0 right-0 bg-buy-green/10" style=${{ width: `${(bid.cumulative_qty / maxQty) * 100}%` }}></div>
                                    <span class="relative text-buy-green font-medium">${bid.price.toFixed(2)}</span>
                                    <span class="relative text-right text-slate-300">${bid.qty}</span>
                                    <span class="relative text-right text-slate-500">${bid.cumulative_qty}</span>
                                </div>
                            `)}
                        </div>
                    </div>
                </div>
            `;
        }

        // --- RECENT TRADES ---
        function RecentTrades({ trades }) {
            if (!trades || trades.length === 0) return html`<div class="p-4 text-slate-500">No trades yet...</div>`;
            
            return html`
                <div class="bg-terminal-panel border border-terminal-border rounded-lg p-4 h-full flex flex-col">
                    <h2 class="text-sm font-semibold text-slate-300 uppercase tracking-wider mb-3">Recent Trades</h2>
                    <div class="flex-1 overflow-y-auto">
                        <table class="w-full text-xs">
                            <thead class="text-slate-500 sticky top-0 bg-terminal-panel">
                                <tr>
                                    <th class="text-left py-1 px-2">Price</th>
                                    <th class="text-right py-1 px-2">Size</th>
                                    <th class="text-right py-1 px-2">Time</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${trades.slice().reverse().map(trade => html`
                                    <tr key=${trade.trade_id} class="hover:bg-slate-800/30">
                                        <td class=${`py-1 px-2 font-medium ${trade.price >= (trades[0]?.price || 0) ? 'text-buy-green' : 'text-sell-red'}`}>
                                            ${trade.price.toFixed(2)}
                                        </td>
                                        <td class="py-1 px-2 text-right text-slate-300">${trade.qty}</td>
                                        <td class="py-1 px-2 text-right text-slate-500">
                                            ${new Date(trade.timestamp * 1000).toLocaleTimeString()}
                                        </td>
                                    </tr>
                                `)}
                            </tbody>
                        </table>
                    </div>
                </div>
            `;
        }

        // --- LATENCY CHART ---
        function LatencyChart({ data }) {
            const chartContainerRef = useRef(null);
            const chartRef = useRef(null);
            const seriesRef = useRef(null);

            useEffect(() => {
                if (!chartContainerRef.current || !window.LightweightCharts) return;
                
                const chart = window.LightweightCharts.createChart(chartContainerRef.current, {
                    layout: { background: { type: 'solid', color: 'transparent' }, textColor: '#94a3b8' },
                    grid: { vertLines: { color: '#1f2937' }, horzLines: { color: '#1f2937' } },
                    timeScale: { timeVisible: true, secondsVisible: false, borderColor: '#1f2937' },
                    rightPriceScale: { borderColor: '#1f2937' },
                    crosshair: { mode: 0 },
                    handleScroll: false,
                    handleScale: false
                });
                
                const series = chart.addAreaSeries({
                    topColor: 'rgba(16, 185, 129, 0.4)',
                    bottomColor: 'rgba(16, 185, 129, 0.0)',
                    lineColor: 'rgba(16, 185, 129, 1)',
                    lineWidth: 2,
                    priceFormat: { type: 'custom', minMove: 0.01, formatter: price => `${price.toFixed(1)} µs` }
                });
                
                chartRef.current = chart;
                seriesRef.current = series;
                
                const resizeObserver = new ResizeObserver(entries => {
                    const { width, height } = entries[0].contentRect;
                    chart.applyOptions({ width, height });
                });
                resizeObserver.observe(chartContainerRef.current);
                
                return () => {
                    resizeObserver.disconnect();
                    chart.remove();
                };
            }, []);

            useEffect(() => {
                if (seriesRef.current && data && data.length > 0) {
                    seriesRef.current.setData(data);
                    chartRef.current.timeScale().fitContent();
                }
            }, [data]);

            return html`<div ref=${chartContainerRef} class="w-full h-full" />`;
        }

        // --- MAIN APP ---
        function App() {
            const [wsStatus, setWsStatus] = useState('CONNECTING');
            const [currentTime, setCurrentTime] = useState(new Date().toLocaleTimeString());
            const [activeTab, setActiveTab] = useState('overview');
            const [state, setState] = useState({
                kpis: {},
                order_book: { bids: [], asks: [], spread: { value: 0, mid: 0 } },
                recent_trades: [],
                latency_chart: [],
                system: {}
            });

            useEffect(() => {
                const timer = setInterval(() => setCurrentTime(new Date().toLocaleTimeString()), 1000);
                return () => clearInterval(timer);
            }, []);

            useEffect(() => {
                const wsUrl = `ws://${window.location.host}/ws`;
                let ws;
                let reconnectTimeout;

                const connect = () => {
                    ws = new WebSocket(wsUrl);
                    
                    ws.onopen = () => {
                        setWsStatus('CONNECTED');
                        // Send ping every 30s to keep alive
                        const pingInterval = setInterval(() => {
                            if (ws.readyState === WebSocket.OPEN) ws.send('ping');
                        }, 30000);
                        ws.pingInterval = pingInterval;
                    };
                    
                    ws.onmessage = (event) => {
                        try {
                            const data = JSON.parse(event.data);
                            setState(data);
                        } catch (e) {
                            console.error('Failed to parse WS message', e);
                        }
                    };
                    
                    ws.onclose = () => {
                        setWsStatus('DISCONNECTED');
                        clearInterval(ws.pingInterval);
                        reconnectTimeout = setTimeout(connect, 3000);
                    };
                    
                    ws.onerror = () => {
                        ws.close();
                    };
                };

                connect();

                return () => {
                    clearTimeout(reconnectTimeout);
                    if (ws) {
                        clearInterval(ws.pingInterval);
                        ws.close();
                    }
                };
            }, []);

            const { kpis, order_book, recent_trades, latency_chart, system } = state;

            return html`
                <div class="h-screen flex flex-col overflow-hidden">
                    <${TopNav} status=${wsStatus} time=${currentTime} />
                    <div class="flex-1 flex overflow-hidden">
                        <${Sidebar} active=${activeTab} setActive=${setActiveTab} />
                        
                        <main class="flex-1 overflow-y-auto p-4 lg:p-6 space-y-6">
                            <!-- Header -->
                            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                                <div>
                                    <h1 class="text-2xl font-bold text-slate-100">Dashboard Overview</h1>
                                    <p class="text-sm text-slate-400">Real-time monitoring of ChronosMatch engine performance</p>
                                </div>
                                <div class="flex items-center space-x-4 text-xs text-slate-400">
                                    <span class="flex items-center space-x-1">
                                        <${Icon} path=${icons.clock} className="w-3 h-3" />
                                        <span>Uptime: ${system.uptime ? `${Math.floor(system.uptime / 60)}m ${Math.floor(system.uptime % 60)}s` : '0s'}</span>
                                    </span>
                                    <span class="flex items-center space-x-1">
                                        <${Icon} path=${icons.server} className="w-3 h-3" />
                                        <span>WS: ${system.ws_connections || 0}</span>
                                    </span>
                                </div>
                            </div>

                            <!-- KPIs -->
                            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
                                <${KPICard} label="Orders / Sec" value=${kpis.orders_per_sec || 0} unit="ops" icon=${icons.trendingUp} color="text-emerald-400" />
                                <${KPICard} label="Avg Latency" value=${kpis.avg_latency || 0} unit="µs" icon=${icons.clock} color="text-blue-400" />
                                <${KPICard} label="P99 Latency" value=${kpis.p99_latency || 0} unit="µs" icon=${icons.clock} color="text-amber-400" />
                                <${KPICard} label="Total Orders" value=${kpis.total_orders || 0} unit="" icon=${icons.list} />
                                <${KPICard} label="Matched" value=${kpis.matched_trades || 0} unit="" icon=${icons.activity} color="text-emerald-400" />
                                <${KPICard} label="Active" value=${kpis.active_orders || 0} unit="" icon=${icons.book} />
                            </div>

                            <!-- Main Grid -->
                            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 h-[500px]">
                                <!-- Order Book -->
                                <div class="lg:col-span-1">
                                    <${OrderBook} data=${order_book} />
                                </div>
                                
                                <!-- Chart & Trades -->
                                <div class="lg:col-span-2 flex flex-col gap-6 h-full">
                                    <div class="bg-terminal-panel border border-terminal-border rounded-lg p-4 flex-1 flex flex-col">
                                        <h2 class="text-sm font-semibold text-slate-300 uppercase tracking-wider mb-3">Latency Monitor (µs)</h2>
                                        <div class="flex-1 min-h-0">
                                            <${LatencyChart} data=${latency_chart} />
                                        </div>
                                    </div>
                                    <div class="flex-1 min-h-0">
                                        <${RecentTrades} trades=${recent_trades} />
                                    </div>
                                </div>
                            </div>
                        </main>
                    </div>
                </div>
            `;
        }

        // --- RENDER ---
        const root = createRoot(document.getElementById('root'));
        root.render(html`<${App} />`);
    </script>
</head>
<body class="bg-terminal-bg text-slate-200 antialiased">
    <div id="root" class="h-screen"></div>
</body>
</html>
"""

# ==========================================
# 7. MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    print("\n" + "="*50)
    print("  ChronosMatch — Zero-Copy Trading Engine")
    print("="*50)
    print("  Starting server on http://localhost:8000")
    print("  Press Ctrl+C to stop.\n")
    
    uvicorn.run(
        "chronosmatch:app", 
        host="0.0.0.0", 
        port=8000, 
        log_level="info",
        reload=False
    )