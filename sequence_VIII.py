"""Sequence VIII"""
num = int(input())
COUNT = 1
for i in range(num):
    for j in range(i, num - 1):
        print("  ", end=" ")

    for j in range(i + 1):
        print(f"{COUNT:>02}", end=" " if j != i else "")
        COUNT += 1
    print()
    COUNT = 1
