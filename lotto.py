"""Lotto"""

one = input()
Last_two = int(input())
page_three1 = int(input())
page_three2 = int(input())
Last_three1 = int(input())
Last_three2 = int(input())
lotto = input()
money = 0
p = int(one)-1
t = int(one)+1
p = f"{p:06}"
t = f"{t:06}"

if one == "000000" and lotto in ("999999", "000001"):
    money += 100000
elif one == "999999" and lotto in ("999998", "000000"):
    money += 100000
elif lotto in (p, t):
    money += 100000

if lotto == one:
    money += 6000000

if int(lotto[4:]) == Last_two:
    money += 2000

if int(lotto[0:3]) == page_three1 and int(lotto[0:3]) == page_three2:
    money += 8000
elif int(lotto[0:3]) == page_three1 or int(lotto[0:3]) == page_three2:
    money += 4000

if int(lotto[3:]) == Last_three1 and int(lotto[3:]) == Last_three2:
    money += 8000
elif int(lotto[3:]) == Last_three1 or int(lotto[3:]) == Last_three2:
    money += 4000
print(money)
