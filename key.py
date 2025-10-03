"""Key"""
id_card = input()
PLUS = 0
for i in id_card:
    PLUS += int(i)
MUL = int(id_card[10:]) * 10
RESULT = PLUS + MUL
if len(str(RESULT)) < 4:
    RESULT += 1000
    print(RESULT)
elif len(str(RESULT)) > 4:
    RESULT = str(RESULT)
    print(RESULT[1:])
else:
    print(RESULT)
