"""Digity """
COUNT = 0
KEEPS = {}
def find_digity(num):
    """To find digit"""
    SUM = 0
    while num > 9:
        for w in str(num):
            SUM += int(w)
        num = SUM
        SUM = 0
    return num

while True:
    BEFORE_ZERO = int(input())
    if not BEFORE_ZERO:
        break
    COUNT += 1
    KEEPS[COUNT] = find_digity(BEFORE_ZERO)

for i in range(1, COUNT + 1):
    print(KEEPS[i])
