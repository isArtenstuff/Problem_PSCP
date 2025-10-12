"""Lotto"""
first_price = input()
last_2 = input()
first_31 = input()
first_32 = input()
last_31 = input()
last_32 = input()
my_lotto = input()
PRICE = 0
CLOSE_PLUS = str(int(first_price) + 1)
CLOSE_SUB = str(int(first_price) - 1)
if first_price == "000000":
    CLOSE_PLUS = "000001"
    CLOSE_SUB = "999999"
if my_lotto == first_price:
    PRICE += 6000000
if my_lotto[4:] == last_2:
    PRICE += 2000
if my_lotto[:3] == first_31 or my_lotto[:3] == first_32:
    PRICE += 4000
if my_lotto[3:] == last_31 or my_lotto[3:] == last_32:
    PRICE += 4000
if my_lotto == CLOSE_PLUS or my_lotto == CLOSE_SUB:
    PRICE += 100000
print(PRICE)
