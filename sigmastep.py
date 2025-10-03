"""Sigma step"""
x = int(input())
y = int(input())
n = int(input())
TOTAL = 0
ERROR = False
if (x - y < 0 and n < 0) or (x - y > 0 and n > 0):
    print("error")
elif x == y:
    print(x)
else:
    if not x and not y and not n:
        print(TOTAL)
    else:
        try:
            for i in range(x, y + (1 if n > 0 else -1), n):
                TOTAL += i
        except ValueError:
            ERROR = True
            print("error")
        if not ERROR:
            print(TOTAL)
