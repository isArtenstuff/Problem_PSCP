"""Coke"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
BATH = 0
CAPS = 0
i = 0
while i < d:
    if 0 < b <= CAPS:
        BATH += c
        CAPS = CAPS - b + 1
    else:
        BATH += a
        CAPS += 1
    i += 1
print(BATH)
