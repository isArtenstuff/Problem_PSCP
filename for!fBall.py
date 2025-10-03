"""For !F Ball"""
change = input()
FIRST = True
SECOND = False
THIRD = False
for i in change :
    match i :
        case "A" :
            FIRST, SECOND = SECOND, FIRST
            continue
        case "B" :
            SECOND, THIRD = THIRD, SECOND
            continue
        case "C" :
            THIRD, FIRST = FIRST, THIRD
            continue
        case _ :
            break
if FIRST :
    print(1)
elif SECOND :
    print(2)
elif THIRD :
    print(3)
