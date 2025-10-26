"""Matrix MN"""
row = int(input())
column = int(input())

MATRIX = []

for r in range(row):
    r += 1
    ROW_LIST = []
    for c in range(column):
        c += 1
        NUM = int(input())
        ROW_LIST.append(str(NUM))
    MATRIX.append(" ".join(ROW_LIST))

for i in MATRIX:
    print(i)
