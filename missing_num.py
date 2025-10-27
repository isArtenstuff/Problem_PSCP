"""Missing Number"""

def main():
    """PSCP - Missing Number"""
    number = int(input())
    a = []
    b = []
    for _ in range(number):
        n = int(input())
        if not n:
            break
        a.append(n)
    for _ in range(1,number+1):
        b.append(_)
    result = list(set(b) - set(a))
    result.sort()
    for i in result:
        print(i)

main()
