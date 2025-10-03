"""Sequence III"""
size = int(input())
for i in range(2, size + 2):
    num = i
    for j in range(size):
        if j != size - 1:
            print(num, end=" ")
        else:
            print(num, end="")
        num += 1
    print()
