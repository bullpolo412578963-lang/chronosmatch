# python compound interest calculation

principle = 0
rate = 0
time = 0

# Principal input
while True:
    principle = float(input("Enter the principal amount: "))
    if principle < 0:
        print("Principal cannot be less than zero")
    else:
        break

# Rate input
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate cannot be less than zero")
    else:
        break

# Time input
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time cannot be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year(s): ${total:.2f}")