"""Tuple's Sad Life"""

def main():
    """PSCP - Tuple's Sad Life"""
    tuple_n = tuple(input().split())
    number = input()
    text = tuple_n.count(number)
    indextup = tuple_n.index(number)

    if tuple_n == 1:
        print(indextup)
        return
    for _ in range(text):
        for j in range(1,text+1):
            if j == text:
                print(indextup,end="")
            else:
                print(indextup,end=" ")
        print()
main()
