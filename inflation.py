"""Inflation"""
price = int(float(input()) * 100)
year = int(input())
for i in range(year):
    total_per_year = (price * 381) // 10000
    price += total_per_year
    i += i
front_int = price // 100
decimal = price % 100
print(f"{front_int}.{decimal:02d}")
