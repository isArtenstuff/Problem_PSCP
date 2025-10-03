"""Coin Change v1"""
change = int(input())
def find_atleast(x):
    """To find atleast coin"""
    COUNT = 0
    while x:
        if x >= 25:
            FIR = x // 25
            COUNT += FIR
            x -= 25 * FIR
        elif x >= 10:
            SEC = x // 10
            COUNT += SEC
            x -= 10 * SEC
        elif x >= 5:
            THI = x // 5
            COUNT += THI
            x -= 5 * THI
        else:
            COUNT += x
            x = 0
    print(COUNT)
find_atleast(change)
