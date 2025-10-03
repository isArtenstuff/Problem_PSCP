"""Bill"""
TOTLE = int(input())
SER = (TOTLE * 10) / 100
if SER < 50 :
    SER = 50
elif SER > 1000 :
    SER = 1000
vat = ((TOTLE + SER) * 7) / 100
bill = TOTLE + SER + vat
print(f"{bill:.2f}")
