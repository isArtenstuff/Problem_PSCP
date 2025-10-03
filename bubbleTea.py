"""Bubble"""
bubble = input()
tea = input()
CAL = 0
if "H" in bubble :
    CAL += int(bubble[2:]) * 5
elif "O" in bubble :
    CAL += int(bubble[2:]) * 3
elif "J" in bubble :
    CAL += int(bubble[2:]) * 2
if "R" in tea :
    if tea[2] in "1" :
        CAL += int(tea[4:]) * 12
    if tea[2] in "2" :
        CAL += int(tea[4:]) * 18
    if tea[2] in "3" :
        CAL += int(tea[4:]) * 25
elif "T" in tea :
    if tea[2] in "1" :
        CAL += int(tea[4:]) * 15
    if tea[2] in "2" :
        CAL += int(tea[4:]) * 20
    if tea[2] in "3" :
        CAL += int(tea[4:]) * 30
elif "M" in tea :
    if tea[2] in "1" :
        CAL += int(tea[4:]) * 10
    if tea[2] in "2" :
        CAL += int(tea[4:]) * 15
    if tea[2] in "3" :
        CAL += int(tea[4:]) * 20
print(CAL)
