"""GQuuuuuux"""

text = input()
LIST_NUM = []
NUM = 0
SCORE = 0
UP = ""
for i in text:
    UP = i.upper()
    if UP == "X":
        if not NUM:
            continue
        LIST_NUM.append(NUM)
        SCORE = 0
        NUM = 0
        continue
    if UP == "U" and SCORE == 2:
        NUM += 1
        continue
    if SCORE == 2:
        SCORE = 0
        NUM = 0

    if UP == "G" and not SCORE:
        SCORE += 1
    elif UP == "Q" and SCORE == 1:
        SCORE += 1
    else:
        if UP == "G":
            continue
        SCORE = 0
if not LIST_NUM:
    print("None")
else:
    print(max(LIST_NUM))
