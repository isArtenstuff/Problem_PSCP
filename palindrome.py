"""Palindrome"""

number = int(input())
time = input()
HOUR = 0
N = 0
TEXT = 0
SAVE_FIRST = ""
if time[1] == ":":
    HOUR = int(time[0])
    N = int(time[2:])
else:
    HOUR = int(time[0:2])
    N = int(time[3:])
while N < 60:
    N += 1
    if N == 60:
        HOUR += 1
        N = 0
    if HOUR == 24:
        HOUR = 0
        N = 0
    SAVE_FIRST = str(HOUR)+str(f"{N:02d}")
    # print(save_1,save_2)
    if SAVE_FIRST == SAVE_FIRST[::-1]:
        print(str(HOUR)+":"+str(f"{N:02d}"))
        TEXT += 1
    if TEXT == number:
        break
