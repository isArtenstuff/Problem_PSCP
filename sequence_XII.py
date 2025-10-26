"""Sequence XII"""

num = int(input())


OPE = ["+"] * (num * 2 - 1)
MAIN_LIST = [""] * (num * 2 - 1)

def funny_math(col: int, val: int) -> None:
    """docstring"""
    if MAIN_LIST[col]:
        x = int(MAIN_LIST[col])
        expected_num = x - 1 if OPE[col] == "-" else x + 1
    else:
        expected_num = val

    MAIN_LIST[col] = f"{expected_num:02d}"


    cur = int(MAIN_LIST[col])
    if cur == num:
        OPE[col] = "-"
    elif cur == 1:
        OPE[col] = "+"

# Top
TOP = []
for i in range(num - 1):
    column = 0
    for current in range(num, 1, -1):
        funny_math(column, current)
        column += 1
    for current in range(1, num + 1):
        funny_math(column, current)
        column += 1
    TOP.append(MAIN_LIST.copy())
    i += 1

for row in TOP:
    print(" ".join(row))

# Middle
MID = [f"{i:02d}" for i in range(1, num)]
MID.append(f"{num:02d}")
MID.extend(f"{i:02d}" for i in range(num - 1, 0, -1))
print(" ".join(MID))

# Bottom
TOP.reverse()
for row in TOP:
    print(" ".join(row))
