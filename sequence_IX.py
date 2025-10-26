"""Sequence IX"""

number = int(input())
for i in range(1, number + 1):
    print("   " * (number - i), end="")
    for j in range(1, i + 1):
        if i == 1:
            print(f"{j:02}", end="")
        else:
            print(f"{j:02}", end=" ")
    for j in range(i - 1, 0, -1):
        if j == 1:
            print(f"{j:02}", end="")
        else:
            print(f"{j:02}", end=" ")
    print()
