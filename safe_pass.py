"""Check key"""
char = input()
digit = input()
if char == "H" and digit == "4567" :
    print("safe unlocked")
elif char == "H" and digit != "4567" :
    print("safe locked - change digit")
elif char != "H" and digit == "4567" :
    print("safe locked - change char")
else :
    print("safe locked")
