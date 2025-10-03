"""Left arrow"""
import math
k = int(input())
n = int(input())
MID = math.ceil(n / 2)
for i in range(1, n + 1):
    SPACE = abs(MID - i) * " "
    OUTPUT = SPACE + "*" * k
    print(OUTPUT)
