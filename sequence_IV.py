"""Sequence IV"""
size = int(input())
NUM = 1
COUNT = 0
for i in range(1, size + 1):
    COUNT = NUM
    for j in range(size):
        if j != size - 1:
            print(COUNT, end=" ")
        else:
            print(COUNT, end="")
        COUNT += 1
    NUM += size
    i += 1
    print()
