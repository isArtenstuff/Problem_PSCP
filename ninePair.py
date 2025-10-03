"""999"""
N = int(input())
code1 = input()
code2 = input()
def main() :
    """pairing"""
    wrong_count = 0

    for i in range(N):
        digit1 = int(code1[i])
        digit2 = int(code2[i])
        if digit1 + digit2 != 9:
            wrong_count += 1

    if not wrong_count :
        print("YES")
    else:
        print("NO", wrong_count)
main()
