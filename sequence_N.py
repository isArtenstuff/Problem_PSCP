"""Sequence N"""
size = int(input())
for r in range(size):
    for c in range(size):
        if c == r or not c or c == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
