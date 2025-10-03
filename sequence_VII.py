"""Sequence VII"""
num = int(input())
COUNT = 1
for i in range(num):
    for j in range(i + 1):
        print(COUNT, end=" " if j != i else "")
        COUNT += 1
    print()
    COUNT = 1
for i in range (1, num):
    for j in range(i, num):
        print(COUNT, end=" " if j != num - 1 else "")
        COUNT += 1
    print()
    COUNT = 1
