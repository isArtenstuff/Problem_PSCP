"""Stroke Zero"""
total_line = int(input())
for i in range(total_line):
    for j in range(i + 1):
        if total_line - 1 > i > 1:
            num = j + 1
            if num == 1:
                print("0", end=" ")
            elif num == i + 1:
                print("0", end="")
            else:
                print("1",end=" ")
        else:
            if not i:
                print("0", end="")
            else:
                if j == i:
                    print("0", end="")
                else:
                    print("0", end=" ")
    print()
