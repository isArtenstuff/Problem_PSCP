"""Last Stand"""


def main():
    """PSCP - Last Stand"""
    num = input()
    num = num.strip("[]")
    num = list(map(str, num.split(",")))
    for i in num:
        print(i[-1])

main()
