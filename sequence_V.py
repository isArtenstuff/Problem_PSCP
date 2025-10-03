"""Sequence V"""
num = int(input())
FINISH = False
while num >= 1 and FINISH is False:
    for i in range(7):
        print(num, end=" " if i != 6 else "")
        if num == 1:
            FINISH = True
            break
        num -= 1
    print()
