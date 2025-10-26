"""Sequence XI"""

n = int(input())
SIZE = 2 * n - 1

for i in range(SIZE):
    row = []
    for j in range(SIZE):
        num = min(i, j, SIZE - 1 - i, SIZE - 1 - j) + 1
        row.append(f"{num:02d}")
    print(" ".join(row))
