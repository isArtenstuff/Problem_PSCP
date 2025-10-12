"""Pig"""
n = int(input())
weight = list(map(int, input().split()))

GREATER_LIST = [] #สร้างไว้ใส่maxของแต่ละคู่

for i in range(n): #เก็บค่าmaxของแต่ละคู่เรียบร้อย
    W1 = weight[i * 2]
    W2 = weight[i * 2 + 1]
    GREATER = max(W1, W2)
    GREATER_LIST.append(GREATER)

TOTAL = sum(GREATER_LIST) #ผลรวมน้ำหนักหมูทั้งหมด

if n > 1: #ถ้ามีมากกว่า 1 คู่ให้เขียนแบบสมการ
    EQUATION = " + ".join(str(x) for x in GREATER_LIST)
    print(f"{EQUATION} = {TOTAL}")
else: #คู่เดียวเขียนตำตอบเลย
    print(TOTAL)
