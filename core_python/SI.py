p = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate: "))
t = float(input("Enter the time: "))
unit =input("Enter the unit: ")
if unit == "day":
    t = t / 365
elif unit == "month":
    t = t / 12
else:
    print("Invalid unit!")
    exit()
def simple_interest(p, r, t):
    return (p * r * t) / 100
def compound_interest(p, r, t):
    amount = p * (1 + r / 100) ** t
    return amount - p
si = simple_interest(p, r, t)
ci = compound_interest(p, r, t)

print("Simple Interest =", si)
print("Compound Interest =", ci)