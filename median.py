
"""Mdedian"""
data = input().split(", ")
numbers = [float(x) for x in data]

numbers.sort()

n = len(numbers)

if n % 2:
    median = numbers[n // 2]
else:
    po1 = numbers[n // 2 - 1]
    po2 = numbers[n // 2]
    median = (po1 + po2) / 2
print(f"{median:.2f}")
