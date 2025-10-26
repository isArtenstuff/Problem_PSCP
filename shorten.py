"""docstring"""

FIRST = ""
LAST = ""
SAVE_NUM = ""
STATE = True
FIS_INP = True
INDEX = 0
COUNT = 0

while STATE:
    try:
        number = input()
    except EOFError:
        break
    if len(number) > 0:
        number = int(number)
    else:
        continue

    if FIS_INP:
        FIRST += str(number)
        INDEX = number + 1
        FIS_INP = False
        continue

    if number <= -1:
        if not COUNT:
            SAVE_NUM += FIRST
        else:
            FIRST += "-" + str(LAST)
            SAVE_NUM += FIRST
        STATE = False
        continue

    if INDEX == number:
        INDEX += 1
        COUNT += 1
        LAST = str(number)
        continue
    if not COUNT:
        SAVE_NUM += FIRST + ", "
    else:
        FIRST += "-" + str(LAST) + ", "
        SAVE_NUM += FIRST
    COUNT = 0
    FIRST = str(number)
    LAST = str(number)
    INDEX = number + 1

print(SAVE_NUM)
