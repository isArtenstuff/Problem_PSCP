"""Donut"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
RORB = d // (b + c)
DONUT = RORB * (b + c)
BATH = RORB * b * a
REMAIN = d % (b + c)

if REMAIN :
    if REMAIN >= b:
        DONUT += b + c
        BATH += a * b
    else:
        DONUT += REMAIN
        BATH += REMAIN *a
print(f"{BATH} {DONUT}")
