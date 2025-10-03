"""Tax"""
income = int(input())

TAX = 0

brackets = [
    (0, 150000, 0),
    (150001, 300000, 0.05),
    (300001, 500000, 0.10),
    (500001, 750000, 0.15),
    (750001, 1000000, 0.20),
    (1000001, 2000000, 0.25),
    (2000001, 4000000, 0.30),
    (4000001, float('inf'), 0.35)
]

for lower, upper, rate in brackets:
    if income > lower:
        taxable_income = min(income, upper) - lower + (0 if not lower else 1)
        TAX += taxable_income * rate
    else:
        break

print(int(TAX))
