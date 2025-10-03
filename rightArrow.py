"""Right Arrow"""
row = int(input())
column = int(input())
MIDDLE = column // 2
for i in range(MIDDLE):
    for j in range(i):
        print(" ", end="")
        j += 1
    print("*" * row)
print(f"{" " * MIDDLE}{"*" * row}")
for i in range(MIDDLE):
    for j in range(i, MIDDLE - 1):
        print(" ", end="")
        j += 1
    print("*" * row)
