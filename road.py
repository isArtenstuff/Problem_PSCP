"""USA Road"""
num = int(input())
def major_road(number):
    """Check is it not Others"""
    return 1 <= number <= 99 and (not number % 5)
if 1 <= num <= 99:
    if not num % 10:
        print("Horizontal Major Interstate")
        print(f"I-{num}")
    elif not num % 5:
        print("Vertical Major Interstate")
        print(f"I-{num}")
    else:
        print("Others")
elif 100 <= num <= 999:
    FIRST_NUM = num // 100
    OTHERS_NUM = num % 100
    if major_road(OTHERS_NUM):
        if not FIRST_NUM % 2:
            print("Even Minor Interstate")
        else:
            print("Odd Minor Interstate")
        print(f"I-{OTHERS_NUM}")
    else:
        print("Others")
else:
    print("Others")
