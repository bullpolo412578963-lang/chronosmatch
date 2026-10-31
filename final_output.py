def repeat(c, n):
    s = ''
    i = 0
    while i < n:
        s += c
        i += 1
    return s

def line1():
    out = ''
    out += repeat('=', 79)
    out += repeat('+', 3)
    out += repeat('=', 1)
    out += repeat('+', 25)
    out += repeat('*', 1)
    out += repeat('+', 5)
    out += repeat('*', 5)
    out += repeat('+', 9)
    out += repeat('=', 72)
    return out

def line2():
    out = ''
    out += repeat('=', 76)
    out += repeat('+', 1)
    out += repeat('=', 1)
    out += repeat('+', 10)
    out += repeat('*', 10)
    out += repeat('+', 9)
    out += repeat('*', 5)
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('#', 4)
    out += repeat('*', 3)
    out += repeat('+', 8)
    out += repeat('=', 5)
    out += repeat('+', 1)
    out += repeat('=', 65)
    return out

def line3():
    out = ''
    out += repeat('=', 73)
    out += repeat('+', 10)
    out += repeat('*', 3)
    out += repeat('#', 6)
    out += repeat('*', 8)
    out += repeat('+', 8)
    out += repeat('*', 3)
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('*', 5)
    out += repeat('#', 2)
    out += repeat('*', 5)
    out += repeat('+', 5)
    out += repeat('=', 1)
    out += repeat('+', 5)
    out += repeat('=', 62)
    return out

def line4():
    out = ''
    out += repeat('=', 71)
    out += repeat('+', 7)
    out += repeat('*', 3)
    out += repeat('#', 5)
    out += repeat('*', 17)
    out += repeat('+', 6)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('*', 17)
    out += repeat('+', 11)
    out += repeat('=', 60)
    return out

def line5():
    out = ''
    out += repeat('=', 70)
    out += repeat('+', 5)
    out += repeat('*', 2)
    out += repeat('#', 2)
    out += repeat('*', 22)
    out += repeat('+', 3)
    out += repeat('*', 4)
    out += repeat('+', 22)
    out += repeat('*', 6)
    out += repeat('+', 5)
    out += repeat('=', 59)
    return out

def line6():
    out = ''
    out += repeat('=', 69)
    out += repeat('+', 4)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('*', 16)
    out += repeat('+', 13)
    out += repeat('*', 5)
    out += repeat('+', 4)
    out += repeat('*', 1)
    out += repeat('+', 3)
    out += repeat('*', 16)
    out += repeat('+', 1)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 4)
    out += repeat('=', 58)
    return out

def line7():
    out = ''
    out += repeat('=', 67)
    out += repeat('+', 4)
    out += repeat('#', 3)
    out += repeat('*', 5)
    out += repeat('#', 6)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 14)
    out += repeat('+', 15)
    out += repeat('*', 6)
    out += repeat('#', 7)
    out += repeat('*', 7)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('=', 58)
    return out

def line8():
    out = ''
    out += repeat('=', 66)
    out += repeat('+', 3)
    out += repeat('*', 1)
    out += repeat('#', 3)
    out += repeat('*', 4)
    out += repeat('#', 6)
    out += repeat('*', 19)
    out += repeat('+', 16)
    out += repeat('*', 5)
    out += repeat('#', 1)
    out += repeat('*', 14)
    out += repeat('#', 3)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('=', 56)
    return out

def line9():
    out = ''
    out += repeat('=', 65)
    out += repeat('+', 3)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('*', 2)
    out += repeat('#', 5)
    out += repeat('*', 21)
    out += repeat('+', 18)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('*', 9)
    out += repeat('#', 1)
    out += repeat('*', 4)
    out += repeat('#', 3)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('=', 55)
    return out

def line10():
    out = ''
    out += repeat('=', 63)
    out += repeat('+', 4)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('#', 4)
    out += repeat('*', 2)
    out += repeat('#', 6)
    out += repeat('*', 22)
    out += repeat('+', 18)
    out += repeat('*', 14)
    out += repeat('#', 1)
    out += repeat('*', 4)
    out += repeat('#', 3)
    out += repeat('+', 3)
    out += repeat('=', 54)
    return out

def line11():
    out = ''
    out += repeat('=', 62)
    out += repeat('+', 3)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 4)
    out += repeat('*', 3)
    out += repeat('#', 6)
    out += repeat('*', 22)
    out += repeat('+', 19)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('*', 14)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('=', 54)
    return out

def line12():
    out = ''
    out += repeat('=', 62)
    out += repeat('+', 3)
    out += repeat('#', 6)
    out += repeat('*', 4)
    out += repeat('#', 6)
    out += repeat('*', 23)
    out += repeat('+', 18)
    out += repeat('*', 17)
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('#', 3)
    out += repeat('+', 3)
    out += repeat('=', 53)
    return out

def line13():
    out = ''
    out += repeat('=', 61)
    out += repeat('+', 3)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 6)
    out += repeat('#', 8)
    out += repeat('*', 25)
    out += repeat('+', 17)
    out += repeat('*', 15)
    out += repeat('+', 1)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('+', 3)
    out += repeat('=', 53)
    return out

def line14():
    out = ''
    out += repeat('=', 60)
    out += repeat('+', 3)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 7)
    out += repeat('%', 1)
    out += repeat('#', 8)
    out += repeat('*', 28)
    out += repeat('+', 14)
    out += repeat('*', 19)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('+', 3)
    out += repeat('=', 52)
    return out

def line15():
    out = ''
    out += repeat('=', 60)
    out += repeat('+', 3)
    out += repeat('%', 2)
    out += repeat('#', 9)
    out += repeat('*', 1)
    out += repeat('#', 7)
    out += repeat('*', 21)
    out += repeat('+', 1)
    out += repeat('*', 15)
    out += repeat('+', 4)
    out += repeat('*', 16)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('+', 3)
    out += repeat('=', 51)
    return out

def line16():
    out = ''
    out += repeat('=', 61)
    out += repeat('+', 2)
    out += repeat('#', 10)
    out += repeat('*', 1)
    out += repeat('#', 10)
    out += repeat('*', 18)
    out += repeat('+', 4)
    out += repeat('*', 33)
    out += repeat('#', 1)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 3)
    out += repeat('=', 51)
    return out

def line17():
    out = ''
    out += repeat('=', 60)
    out += repeat('+', 2)
    out += repeat('*', 1)
    out += repeat('#', 8)
    out += repeat('*', 1)
    out += repeat('#', 13)
    out += repeat('*', 16)
    out += repeat('+', 5)
    out += repeat('*', 31)
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('=', 52)
    return out

def line18():
    out = ''
    out += repeat('=', 60)
    out += repeat('+', 3)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('#', 20)
    out += repeat('*', 16)
    out += repeat('+', 6)
    out += repeat('*', 32)
    out += repeat('#', 1)
    out += repeat('*', 4)
    out += repeat('#', 2)
    out += repeat('+', 3)
    out += repeat('=', 51)
    return out

def line19():
    out = ''
    out += repeat('=', 61)
    out += repeat('+', 3)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('#', 17)
    out += repeat('*', 14)
    out += repeat('#', 2)
    out += repeat('*', 6)
    out += repeat('+', 2)
    out += repeat('*', 10)
    out += repeat('+', 1)
    out += repeat('*', 5)
    out += repeat('+', 3)
    out += repeat('*', 18)
    out += repeat('#', 2)
    out += repeat('+', 3)
    out += repeat('=', 51)
    return out

def line20():
    out = ''
    out += repeat('=', 62)
    out += repeat('+', 2)
    out += repeat('*', 1)
    out += repeat('#', 7)
    out += repeat('*', 1)
    out += repeat('#', 11)
    out += repeat('*', 12)
    out += repeat('#', 1)
    out += repeat('%', 6)
    out += repeat('#', 2)
    out += repeat('*', 3)
    out += repeat('#', 3)
    out += repeat('*', 2)
    out += repeat('#', 2)
    out += repeat('*', 27)
    out += repeat('#', 3)
    out += repeat('+', 3)
    out += repeat('=', 52)
    return out

def line21():
    out = ''
    out += repeat('=', 62)
    out += repeat('+', 2)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 4)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 20)
    out += repeat('*', 3)
    out += repeat('#', 1)
    out += repeat('%', 7)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 3)
    out += repeat('%', 1)
    out += repeat('#', 10)
    out += repeat('*', 17)
    out += repeat('#', 1)
    out += repeat('*', 3)
    out += repeat('+', 3)
    out += repeat('=', 52)
    return out

def line22():
    out = ''
    out += repeat('=', 62)
    out += repeat('+', 2)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 5)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 12)
    out += repeat('%', 5)
    out += repeat('@', 3)
    out += repeat('%', 2)
    out += repeat('#', 2)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('%', 3)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('+', 1)
    out += repeat('*', 2)
    out += repeat('#', 4)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('%', 1)
    out += repeat('@', 3)
    out += repeat('%', 2)
    out += repeat('#', 2)
    out += repeat('*', 10)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 5)
    out += repeat('+', 4)
    out += repeat('=', 52)
    return out

def line23():
    out = ''
    out += repeat('=', 63)
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 3)
    out += repeat('*', 1)
    out += repeat('#', 5)
    out += repeat('*', 5)
    out += repeat('#', 4)
    out += repeat('%', 5)
    out += repeat('@', 4)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('%', 3)
    out += repeat('#', 6)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('%', 2)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 5)
    out += repeat('%', 4)
    out += repeat('#', 1)
    out += repeat('*', 10)
    out += repeat('#', 1)
    out += repeat('*', 3)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 4)
    out += repeat('=', 52)
    return out

def line24():
    out = ''
    out += repeat('=', 62)
    out += repeat('+', 3)
    out += repeat('#', 2)
    out += repeat('%', 1)
    out += repeat('@', 3)
    out += repeat('%', 1)
    out += repeat('#', 9)
    out += repeat('*', 4)
    out += repeat('#', 4)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 6)
    out += repeat('#', 8)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('*', 5)
    out += repeat('#', 4)
    out += repeat('%', 4)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 4)
    out += repeat('*', 11)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 3)
    out += repeat('=', 53)
    return out

def line25():
    out = ''
    out += repeat('=', 62)
    out += repeat('+', 3)
    out += repeat('#', 2)
    out += repeat('%', 1)
    out += repeat('@', 1)
    out += repeat('%', 3)
    out += repeat('#', 7)
    out += repeat('*', 2)
    out += repeat('#', 6)
    out += repeat('*', 9)
    out += repeat('#', 2)
    out += repeat('*', 4)
    out += repeat('#', 4)
    out += repeat('+', 3)
    out += repeat('*', 4)
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('#', 4)
    out += repeat('*', 19)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('*', 3)
    out += repeat('+', 4)
    out += repeat('=', 1)
    out += repeat('+', 3)
    out += repeat('=', 48)
    return out

def line26():
    out = ''
    out += repeat('=', 63)
    out += repeat('+', 2)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('@', 2)
    out += repeat('%', 1)
    out += repeat('#', 7)
    out += repeat('*', 1)
    out += repeat('#', 4)
    out += repeat('*', 13)
    out += repeat('#', 1)
    out += repeat('*', 7)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 3)
    out += repeat('*', 5)
    out += repeat('+', 1)
    out += repeat('*', 23)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('+', 5)
    out += repeat('=', 1)
    out += repeat('+', 3)
    out += repeat('=', 48)
    return out

def line27():
    out = ''
    out += repeat('=', 63)
    out += repeat('+', 3)
    out += repeat('%', 1)
    out += repeat('#', 2)
    out += repeat('%', 1)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('#', 4)
    out += repeat('*', 1)
    out += repeat('#', 3)
    out += repeat('*', 16)
    out += repeat('#', 5)
    out += repeat('*', 4)
    out += repeat('+', 3)
    out += repeat('*', 9)
    out += repeat('+', 12)
    out += repeat('*', 9)
    out += repeat('#', 2)
    out += repeat('*', 2)
    out += repeat('+', 4)
    out += repeat('=', 53)
    return out

def line28():
    out = ''
    out += repeat('=', 63)
    out += repeat('+', 3)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('#', 3)
    out += repeat('*', 1)
    out += repeat('#', 4)
    out += repeat('*', 17)
    out += repeat('#', 2)
    out += repeat('%', 1)
    out += repeat('#', 5)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 4)
    out += repeat('*', 6)
    out += repeat('#', 2)
    out += repeat('*', 4)
    out += repeat('+', 9)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('#', 2)
    out += repeat('*', 2)
    out += repeat('+', 1)
    out += repeat('=', 56)
    return out

def line29():
    out = ''
    out += repeat('=', 64)
    out += repeat('+', 2)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('*', 5)
    out += repeat('#', 3)
    out += repeat('*', 15)
    out += repeat('#', 3)
    out += repeat('%', 3)
    out += repeat('#', 3)
    out += repeat('*', 6)
    out += repeat('+', 2)
    out += repeat('*', 7)
    out += repeat('#', 6)
    out += repeat('*', 4)
    out += repeat('+', 6)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('*', 4)
    out += repeat('+', 3)
    out += repeat('=', 56)
    return out

def line30():
    out = ''
    out += repeat('=', 64)
    out += repeat('+', 3)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 2)
    out += repeat('*', 2)
    out += repeat('#', 4)
    out += repeat('*', 10)
    out += repeat('#', 9)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('%', 5)
    out += repeat('#', 11)
    out += repeat('*', 3)
    out += repeat('#', 8)
    out += repeat('*', 10)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('+', 7)
    out += repeat('=', 55)
    return out

def line31():
    out = ''
    out += repeat('=', 65)
    out += repeat('+', 3)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 8)
    out += repeat('*', 7)
    out += repeat('#', 9)
    out += repeat('*', 2)
    out += repeat('#', 2)
    out += repeat('%', 5)
    out += repeat('#', 10)
    out += repeat('*', 3)
    out += repeat('+', 1)
    out += repeat('*', 2)
    out += repeat('#', 8)
    out += repeat('*', 8)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('+', 6)
    out += repeat('=', 56)
    return out

def line32():
    out = ''
    out += repeat('=', 66)
    out += repeat('+', 3)
    out += repeat('*', 4)
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('#', 4)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('%', 2)
    out += repeat('#', 3)
    out += repeat('*', 2)
    out += repeat('#', 4)
    out += repeat('*', 4)
    out += repeat('#', 7)
    out += repeat('*', 5)
    out += repeat('+', 6)
    out += repeat('*', 4)
    out += repeat('#', 6)
    out += repeat('*', 7)
    out += repeat('#', 3)
    out += repeat('*', 3)
    out += repeat('+', 2)
    out += repeat('=', 57)
    return out

def line33():
    out = ''
    out += repeat('=', 67)
    out += repeat('+', 8)
    out += repeat('#', 8)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 2)
    out += repeat('%', 3)
    out += repeat('@', 4)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 13)
    out += repeat('*', 6)
    out += repeat('#', 6)
    out += repeat('*', 2)
    out += repeat('#', 3)
    out += repeat('*', 8)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('+', 5)
    out += repeat('=', 56)
    return out

def line34():
    out = ''
    out += repeat('=', 68)
    out += repeat('+', 2)
    out += repeat('=', 3)
    out += repeat('+', 2)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('#', 5)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('#', 3)
    out += repeat('%', 2)
    out += repeat('@', 5)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('#', 2)
    out += repeat('%', 6)
    out += repeat('#', 10)
    out += repeat('%', 1)
    out += repeat('@', 1)
    out += repeat('%', 6)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('*', 9)
    out += repeat('+', 8)
    out += repeat('=', 55)
    return out

def line35():
    out = ''
    out += repeat('=', 73)
    out += repeat('+', 3)
    out += repeat('%', 2)
    out += repeat('#', 4)
    out += repeat('%', 2)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('#', 5)
    out += repeat('%', 1)
    out += repeat('@', 3)
    out += repeat('%', 2)
    out += repeat('#', 3)
    out += repeat('+', 1)
    out += repeat('*', 2)
    out += repeat('+', 2)
    out += repeat('*', 1)
    out += repeat('+', 6)
    out += repeat('*', 2)
    out += repeat('#', 2)
    out += repeat('%', 2)
    out += repeat('#', 5)
    out += repeat('*', 3)
    out += repeat('#', 1)
    out += repeat('*', 8)
    out += repeat('+', 8)
    out += repeat('=', 56)
    return out

def line36():
    out = ''
    out += repeat('=', 74)
    out += repeat('+', 3)
    out += repeat('%', 2)
    out += repeat('#', 3)
    out += repeat('%', 3)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('#', 2)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('%', 3)
    out += repeat('#', 2)
    out += repeat('%', 4)
    out += repeat('#', 10)
    out += repeat('*', 5)
    out += repeat('+', 4)
    out += repeat('*', 12)
    out += repeat('+', 4)
    out += repeat('=', 61)
    return out

def line37():
    out = ''
    out += repeat('=', 75)
    out += repeat('+', 3)
    out += repeat('%', 1)
    out += repeat('@', 1)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('%', 5)
    out += repeat('#', 1)
    out += repeat('*', 5)
    out += repeat('#', 17)
    out += repeat('*', 6)
    out += repeat('+', 8)
    out += repeat('*', 10)
    out += repeat('+', 4)
    out += repeat('=', 62)
    return out

def line38():
    out = ''
    out += repeat('=', 75)
    out += repeat('+', 4)
    out += repeat('#', 1)
    out += repeat('%', 2)
    out += repeat('#', 2)
    out += repeat('%', 4)
    out += repeat('#', 1)
    out += repeat('*', 5)
    out += repeat('#', 16)
    out += repeat('*', 8)
    out += repeat('+', 5)
    out += repeat('*', 10)
    out += repeat('+', 4)
    out += repeat('=', 63)
    return out

def line39():
    out = ''
    out += repeat('=', 73)
    out += repeat('+', 6)
    out += repeat('*', 1)
    out += repeat('%', 4)
    out += repeat('#', 1)
    out += repeat('%', 4)
    out += repeat('#', 1)
    out += repeat('*', 6)
    out += repeat('#', 13)
    out += repeat('*', 3)
    out += repeat('#', 1)
    out += repeat('*', 5)
    out += repeat('+', 4)
    out += repeat('*', 11)
    out += repeat('+', 5)
    out += repeat('=', 62)
    return out

def line40():
    out = ''
    out += repeat('=', 70)
    out += repeat('+', 6)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('%', 5)
    out += repeat('#', 1)
    out += repeat('%', 4)
    out += repeat('#', 1)
    out += repeat('*', 9)
    out += repeat('#', 6)
    out += repeat('*', 10)
    out += repeat('+', 4)
    out += repeat('*', 13)
    out += repeat('+', 6)
    out += repeat('=', 60)
    return out

def line41():
    out = ''
    out += repeat('=', 68)
    out += repeat('+', 6)
    out += repeat('#', 1)
    out += repeat('@', 4)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('@', 1)
    out += repeat('%', 11)
    out += repeat('#', 2)
    out += repeat('*', 4)
    out += repeat('+', 1)
    out += repeat('*', 13)
    out += repeat('+', 5)
    out += repeat('*', 15)
    out += repeat('+', 2)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 4)
    out += repeat('=', 59)
    return out

def line42():
    out = ''
    out += repeat('=', 66)
    out += repeat('+', 5)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('@', 5)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('@', 2)
    out += repeat('%', 12)
    out += repeat('#', 4)
    out += repeat('*', 20)
    out += repeat('#', 2)
    out += repeat('*', 13)
    out += repeat('#', 1)
    out += repeat('@', 2)
    out += repeat('%', 1)
    out += repeat('*', 1)
    out += repeat('+', 4)
    out += repeat('=', 57)
    return out

def line43():
    out = ''
    out += repeat('=', 58)
    out += repeat('+', 11)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('@', 7)
    out += repeat('*', 3)
    out += repeat('#', 1)
    out += repeat('@', 2)
    out += repeat('%', 18)
    out += repeat('#', 20)
    out += repeat('*', 13)
    out += repeat('@', 4)
    out += repeat('%', 1)
    out += repeat('*', 1)
    out += repeat('+', 4)
    out += repeat('=', 55)
    return out

def line44():
    out = ''
    out += repeat('=', 49)
    out += repeat('+', 18)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 8)
    out += repeat('%', 1)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 2)
    out += repeat('%', 8)
    out += repeat('#', 2)
    out += repeat('%', 17)
    out += repeat('#', 6)
    out += repeat('*', 2)
    out += repeat('+', 1)
    out += repeat('*', 8)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('*', 1)
    out += repeat('@', 6)
    out += repeat('%', 1)
    out += repeat('*', 1)
    out += repeat('+', 4)
    out += repeat('=', 53)
    return out

def line45():
    out = ''
    out += repeat('=', 41)
    out += repeat('+', 21)
    out += repeat('*', 3)
    out += repeat('#', 1)
    out += repeat('@', 12)
    out += repeat('*', 6)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 3)
    out += repeat('%', 8)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('#', 4)
    out += repeat('%', 7)
    out += repeat('#', 4)
    out += repeat('*', 4)
    out += repeat('#', 10)
    out += repeat('*', 2)
    out += repeat('+', 3)
    out += repeat('#', 1)
    out += repeat('@', 8)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 8)
    out += repeat('=', 47)
    return out

def line46():
    out = ''
    out += repeat('=', 35)
    out += repeat('+', 17)
    out += repeat('*', 3)
    out += repeat('#', 3)
    out += repeat('%', 2)
    out += repeat('@', 18)
    out += repeat('*', 8)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 3)
    out += repeat('%', 5)
    out += repeat('@', 4)
    out += repeat('%', 3)
    out += repeat('#', 4)
    out += repeat('*', 4)
    out += repeat('#', 3)
    out += repeat('%', 6)
    out += repeat('#', 6)
    out += repeat('*', 2)
    out += repeat('+', 6)
    out += repeat('@', 11)
    out += repeat('#', 1)
    out += repeat('+', 14)
    out += repeat('=', 40)
    return out

def line47():
    out = ''
    out += repeat('=', 30)
    out += repeat('+', 14)
    out += repeat('*', 2)
    out += repeat('#', 3)
    out += repeat('%', 2)
    out += repeat('@', 27)
    out += repeat('#', 1)
    out += repeat('*', 10)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 3)
    out += repeat('%', 7)
    out += repeat('@', 14)
    out += repeat('%', 5)
    out += repeat('#', 4)
    out += repeat('*', 2)
    out += repeat('+', 7)
    out += repeat('%', 1)
    out += repeat('@', 13)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('+', 17)
    out += repeat('=', 33)
    return out

def line48():
    out = ''
    out += repeat('=', 25)
    out += repeat('+', 13)
    out += repeat('*', 2)
    out += repeat('#', 2)
    out += repeat('%', 1)
    out += repeat('@', 36)
    out += repeat('*', 12)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 3)
    out += repeat('%', 16)
    out += repeat('@', 3)
    out += repeat('%', 2)
    out += repeat('#', 3)
    out += repeat('*', 3)
    out += repeat('+', 9)
    out += repeat('*', 1)
    out += repeat('@', 19)
    out += repeat('%', 1)
    out += repeat('#', 2)
    out += repeat('*', 2)
    out += repeat('+', 16)
    out += repeat('=', 27)
    return out

def line49():
    out = ''
    out += repeat('=', 20)
    out += repeat('+', 12)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('%', 2)
    out += repeat('@', 42)
    out += repeat('%', 1)
    out += repeat('*', 14)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 3)
    out += repeat('%', 10)
    out += repeat('@', 2)
    out += repeat('%', 3)
    out += repeat('#', 3)
    out += repeat('*', 2)
    out += repeat('+', 12)
    out += repeat('*', 1)
    out += repeat('@', 27)
    out += repeat('%', 1)
    out += repeat('#', 2)
    out += repeat('*', 2)
    out += repeat('+', 15)
    out += repeat('=', 21)
    return out

def line50():
    out = ''
    out += repeat('=', 15)
    out += repeat('+', 12)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('%', 1)
    out += repeat('@', 49)
    out += repeat('#', 1)
    out += repeat('*', 15)
    out += repeat('#', 1)
    out += repeat('%', 13)
    out += repeat('#', 2)
    out += repeat('*', 4)
    out += repeat('+', 14)
    out += repeat('*', 1)
    out += repeat('@', 34)
    out += repeat('%', 2)
    out += repeat('#', 2)
    out += repeat('*', 2)
    out += repeat('+', 13)
    out += repeat('=', 16)
    return out

def line51():
    out = ''
    out += repeat('=', 10)
    out += repeat('+', 12)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('%', 1)
    out += repeat('@', 55)
    out += repeat('*', 17)
    out += repeat('%', 1)
    out += repeat('@', 9)
    out += repeat('%', 1)
    out += repeat('#', 3)
    out += repeat('*', 3)
    out += repeat('+', 14)
    out += repeat('*', 1)
    out += repeat('@', 42)
    out += repeat('%', 1)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('+', 12)
    out += repeat('=', 12)
    return out

def line52():
    out = ''
    out += repeat('=', 9)
    out += repeat('+', 8)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('%', 1)
    out += repeat('@', 61)
    out += repeat('*', 12)
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('@', 8)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('*', 3)
    out += repeat('#', 3)
    out += repeat('%', 3)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('+', 10)
    out += repeat('*', 1)
    out += repeat('@', 48)
    out += repeat('%', 2)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('+', 9)
    out += repeat('=', 9)
    return out

def line53():
    out = ''
    out += repeat('=', 8)
    out += repeat('+', 4)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('%', 1)
    out += repeat('@', 67)
    out += repeat('*', 9)
    out += repeat('+', 2)
    out += repeat('*', 1)
    out += repeat('%', 1)
    out += repeat('@', 5)
    out += repeat('%', 1)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 12)
    out += repeat('%', 1)
    out += repeat('*', 1)
    out += repeat('+', 8)
    out += repeat('*', 1)
    out += repeat('@', 54)
    out += repeat('%', 1)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('+', 7)
    out += repeat('=', 7)
    return out

def line54():
    out = ''
    out += repeat('=', 6)
    out += repeat('+', 4)
    out += repeat('#', 1)
    out += repeat('@', 72)
    out += repeat('%', 1)
    out += repeat('*', 6)
    out += repeat('+', 2)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('@', 3)
    out += repeat('*', 1)
    out += repeat('@', 15)
    out += repeat('%', 1)
    out += repeat('*', 4)
    out += repeat('+', 5)
    out += repeat('#', 1)
    out += repeat('@', 60)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 5)
    out += repeat('=', 6)
    return out

def line55():
    out = ''
    out += repeat('=', 5)
    out += repeat('+', 3)
    out += repeat('*', 1)
    out += repeat('@', 75)
    out += repeat('#', 1)
    out += repeat('*', 3)
    out += repeat('+', 2)
    out += repeat('*', 8)
    out += repeat('@', 1)
    out += repeat('#', 1)
    out += repeat('@', 14)
    out += repeat('%', 1)
    out += repeat('*', 8)
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('@', 64)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 4)
    out += repeat('=', 4)
    return out

def line56():
    out = ''
    out += repeat('=', 4)
    out += repeat('+', 3)
    out += repeat('#', 1)
    out += repeat('@', 77)
    out += repeat('*', 2)
    out += repeat('+', 1)
    out += repeat('*', 11)
    out += repeat('@', 9)
    out += repeat('%', 1)
    out += repeat('#', 3)
    out += repeat('*', 12)
    out += repeat('#', 1)
    out += repeat('@', 67)
    out += repeat('%', 1)
    out += repeat('*', 1)
    out += repeat('+', 3)
    out += repeat('=', 3)
    return out

def line57():
    out = ''
    out += repeat('=', 3)
    out += repeat('+', 3)
    out += repeat('%', 1)
    out += repeat('@', 79)
    out += repeat('*', 11)
    out += repeat('#', 1)
    out += repeat('%', 2)
    out += repeat('@', 7)
    out += repeat('#', 1)
    out += repeat('+', 11)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('@', 70)
    out += repeat('%', 1)
    out += repeat('+', 3)
    out += repeat('=', 2)
    return out

def line58():
    out = ''
    out += repeat('=', 2)
    out += repeat('+', 3)
    out += repeat('@', 81)
    out += repeat('%', 1)
    out += repeat('*', 2)
    out += repeat('+', 6)
    out += repeat('%', 1)
    out += repeat('@', 1)
    out += repeat('*', 1)
    out += repeat('@', 1)
    out += repeat('#', 1)
    out += repeat('@', 9)
    out += repeat('*', 1)
    out += repeat('+', 8)
    out += repeat('*', 4)
    out += repeat('#', 1)
    out += repeat('@', 73)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('=', 1)
    return out

def line59():
    out = ''
    out += repeat('=', 1)
    out += repeat('+', 3)
    out += repeat('@', 83)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('+', 4)
    out += repeat('*', 1)
    out += repeat('@', 4)
    out += repeat('*', 1)
    out += repeat('@', 1)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 8)
    out += repeat('%', 1)
    out += repeat('*', 1)
    out += repeat('+', 5)
    out += repeat('*', 4)
    out += repeat('%', 1)
    out += repeat('@', 75)
    out += repeat('+', 3)
    return out

def line60():
    out = ''
    out += repeat('+', 3)
    out += repeat('%', 1)
    out += repeat('@', 84)
    out += repeat('#', 1)
    out += repeat('+', 3)
    out += repeat('*', 1)
    out += repeat('@', 6)
    out += repeat('*', 1)
    out += repeat('#', 3)
    out += repeat('@', 9)
    out += repeat('#', 1)
    out += repeat('+', 3)
    out += repeat('*', 4)
    out += repeat('%', 1)
    out += repeat('@', 76)
    out += repeat('#', 1)
    out += repeat('+', 2)
    return out

def line61():
    out = ''
    out += repeat('+', 2)
    out += repeat('*', 1)
    out += repeat('@', 86)
    out += repeat('*', 1)
    out += repeat('+', 2)
    out += repeat('%', 1)
    out += repeat('@', 8)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('@', 9)
    out += repeat('*', 5)
    out += repeat('@', 78)
    out += repeat('%', 1)
    out += repeat('+', 2)
    return out

def line62():
    out = ''
    out += repeat('+', 2)
    out += repeat('%', 1)
    out += repeat('@', 86)
    out += repeat('%', 1)
    out += repeat('+', 1)
    out += repeat('*', 2)
    out += repeat('@', 10)
    out += repeat('%', 1)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('@', 8)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('@', 80)
    out += repeat('+', 2)
    return out

def line63():
    out = ''
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('@', 88)
    out += repeat('#', 1)
    out += repeat('%', 3)
    out += repeat('*', 1)
    out += repeat('@', 10)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 1)
    out += repeat('%', 1)
    out += repeat('@', 6)
    out += repeat('%', 1)
    out += repeat('*', 1)
    out += repeat('@', 81)
    out += repeat('*', 1)
    out += repeat('+', 1)
    return out

def line64():
    out = ''
    out += repeat('+', 1)
    out += repeat('#', 1)
    out += repeat('@', 89)
    out += repeat('#', 2)
    out += repeat('@', 2)
    out += repeat('*', 1)
    out += repeat('@', 10)
    out += repeat('%', 1)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('@', 5)
    out += repeat('%', 1)
    out += repeat('@', 82)
    out += repeat('*', 1)
    out += repeat('+', 1)
    return out

def line65():
    out = ''
    out += repeat('*', 1)
    out += repeat('@', 92)
    out += repeat('+', 1)
    out += repeat('#', 1)
    out += repeat('%', 2)
    out += repeat('*', 1)
    out += repeat('@', 10)
    out += repeat('#', 1)
    out += repeat('*', 2)
    out += repeat('%', 1)
    out += repeat('@', 86)
    out += repeat('#', 1)
    out += repeat('+', 1)
    return out

def line66():
    out = ''
    out += repeat('%', 1)
    out += repeat('@', 93)
    out += repeat('%', 1)
    out += repeat('+', 1)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('@', 10)
    out += repeat('%', 1)
    out += repeat('*', 2)
    out += repeat('#', 1)
    out += repeat('@', 85)
    out += repeat('#', 1)
    out += repeat('+', 1)
    return out

def line67():
    out = ''
    out += repeat('@', 96)
    out += repeat('#', 1)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('*', 1)
    out += repeat('@', 10)
    out += repeat('+', 1)
    out += repeat('*', 1)
    out += repeat('@', 85)
    out += repeat('%', 1)
    out += repeat('+', 1)
    return out

def line68():
    out = ''
    out += repeat('@', 98)
    out += repeat('*', 3)
    out += repeat('+', 1)
    out += repeat('%', 1)
    out += repeat('@', 9)
    out += repeat('%', 1)
    out += repeat('@', 86)
    out += repeat('*', 1)
    return out

def line69():
    out = ''
    out += repeat('@', 99)
    out += repeat('%', 1)
    out += repeat('+', 1)
    out += repeat('*', 3)
    out += repeat('@', 95)
    out += repeat('#', 1)
    return out

def line70():
    out = ''
    out += repeat('@', 101)
    out += repeat('#', 1)
    out += repeat('*', 4)
    out += repeat('@', 93)
    out += repeat('%', 1)
    return out

def line71():
    out = ''
    out += repeat('@', 103)
    out += repeat('*', 1)
    out += repeat('#', 2)
    out += repeat('+', 1)
    out += repeat('#', 1)
    out += repeat('@', 92)
    return out

def line72():
    out = ''
    out += repeat('@', 104)
    out += repeat('#', 3)
    out += repeat('%', 1)
    out += repeat('*', 1)
    out += repeat('@', 91)
    return out

def line73():
    out = ''
    out += repeat('@', 106)
    out += repeat('+', 1)
    out += repeat('%', 1)
    out += repeat('@', 92)
    return out

def line74():
    out = ''
    out += repeat('@', 107)
    out += repeat('%', 1)
    out += repeat('@', 92)
    return out

def line75():
    return repeat('@', 200)

def line76():
    return repeat('@', 200)

def line77():
    return repeat('@', 200)

functions = [
    line1,
    line2,
    line3,
    line4,
    line5,
    line6,
    line7,
    line8,
    line9,
    line10,
    line11,
    line12,
    line13,
    line14,
    line15,
    line16,
    line17,
    line18,
    line19,
    line20,
    line21,
    line22,
    line23,
    line24,
    line25,
    line26,
    line27,
    line28,
    line29,
    line30,
    line31,
    line32,
    line33,
    line34,
    line35,
    line36,
    line37,
    line38,
    line39,
    line40,
    line41,
    line42,
    line43,
    line44,
    line45,
    line46,
    line47,
    line48,
    line49,
    line50,
    line51,
    line52,
    line53,
    line54,
    line55,
    line56,
    line57,
    line58,
    line59,
    line60,
    line61,
    line62,
    line63,
    line64,
    line65,
    line66,
    line67,
    line68,
    line69,
    line70,
    line71,
    line72,
    line73,
    line74,
    line75,
    line76,
    line77,
]

for f in functions:
    print(f())
