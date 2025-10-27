"""Calculator V2"""

def main():
    """Calculator V2"""
    num = int(input())
    count = 0
    i = 1
    if num == 1:
        print(num)
    else:
        while 10**i <= num:
            count += i * 9 * 10**(i - 1)
            i += 1
        count += i * (num - 10**(i - 1) + 1)
        print(count + num)
main()
