"""Backward"""
TEXTS = []
while True :
    TEXT = str(input())
    if TEXT == "NULL" :
        break
    TEXTS.append(TEXT)
for i in range(len(TEXTS) - 1, -1, -1) :
    print(TEXTS[i])
