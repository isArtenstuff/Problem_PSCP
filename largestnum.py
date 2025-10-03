""" PSCP - Largest Number """
num1 = int(input())
num2 = int(input())
num3 = int(input())

C1 = str(num1) + str(num2) + str(num3)
C2 = str(num1) + str(num3) + str(num2)
C3 = str(num2) + str(num1) + str(num3)
C4 = str(num2) + str(num3) + str(num1)
C5 = str(num3) + str(num2) + str(num1)
C6 = str(num3) + str(num1) + str(num2)

C1 = int(C1)
C2 = int(C2)
C3 = int(C3)
C4 = int(C4)
C5 = int(C5)
C6 = int(C6)

if C1 >= C2 and C1 >= C3 and C1 >= C4 and C1 >= C5 and C1 >= C6:
    print(C1)
elif C2 >= C1 and C2 >= C3 and C2 >= C4 and C2 >= C5 and C2 >= C6:
    print(C2)
elif C3 >= C1 and C3 >= C2 and C3 >= C4 and C3 >= C5 and C3 >= C6:
    print(C3)
elif C4 >= C1 and C4 >= C2 and C4 >= C3 and C4 >= C5 and C4 >= C6:
    print(C4)
elif C5 >= C1 and C5 >= C2 and C5 >= C3 and C5 >= C4 and C5 >= C6:
    print(C5)
else:
    print(C6)
