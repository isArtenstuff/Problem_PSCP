"""Milk"""

def milk_bottle():
    """PSCP - Milk"""
    price = int(input()) # ราคาต่อขวด
    caps = int(input())   # จำนวนฝาที่ใช้แลก
    redeem = int(input())# แลกได้
    pay = int(input())   # เงินที่มี
    ALL_PAY = 0
    FREE = 0
    BOTTLE_PAY = 0
    ADD_FREE = 0
    AFHS = 0
    if price <= 0 or price > pay:
        print(0)
        return
    if caps <= 0:
        ALL_PAY += pay//price
    elif pay >= 0 and 0 <= redeem < caps:
        ALL_PAY += (pay//price)
        FREE += (ALL_PAY // caps) * redeem
        BOTTLE_PAY += ALL_PAY
        while True:
            if BOTTLE_PAY < caps:
                break
            ADD_FREE += (BOTTLE_PAY//caps) * redeem
            AFHS = ((BOTTLE_PAY//caps)*redeem)+(BOTTLE_PAY%caps)
            BOTTLE_PAY = AFHS
    else:
        ALL_PAY += pay//price
    print(ALL_PAY+ADD_FREE)

milk_bottle()
