"""Season"""
month = int(input())
day = int(input())
if month <= 3 :
    if day >= 21 and not month % 3:
        print("spring")
    else:
        print("winter")
elif month <= 6 :
    if day >= 21 and not month % 3:
        print("summer")
    else:
        print("spring")
elif month <= 9 :
    if day >= 21 and not month % 3:
        print("fall")
    else:
        print("summer")
elif month <= 12 :
    if day >= 21 and not month % 3:
        print("winter")
    else:
        print("fall")
