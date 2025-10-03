"""Sort"""
def main() :
    """Sort"""
    how = int(input())
    alll = []
    for _ in range(how) :
        number = int(input())
        alll.append(number)
        alll.sort()
    for number in alll :
        print(number)
main()
