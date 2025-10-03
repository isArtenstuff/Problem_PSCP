"""Sequence I"""
colum = int(input())
row = int(input())
COUNT = 1
for i in range(colum):
    for j in range(row):
        if j == row - 1:
            print(COUNT, end="")
        else:
            print(COUNT, end=" ")
        COUNT += 1
    i += 1
    print()
