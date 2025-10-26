"""Sein Seiya"""

secord = int(input())
punch = int(input())

PUNCH = 0
OUTPUT = 0
T = 1
passpunch = False

while T <= secord:
    if passpunch:
        # print(t)
        sectime = secord - T
        PUNCH += 12 * sectime
        break
    if OUTPUT >= punch:
        passpunch = True
        continue
    if not T % 6:
        OUTPUT = PUNCH
        PUNCH += 1
    elif not T % 2:
        PUNCH += 165
        OUTPUT = PUNCH
    T += 1
print(PUNCH)
