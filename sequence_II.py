"""Sequence II"""
size = int(input())
for i in range(size):
    num = i
    for j in range(size):
        if j != size - 1:
            print(num, end=" ")
        else:
            print(num, end="")
        num += size
    print()
