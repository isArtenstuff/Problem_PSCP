"""Horizontal Histogram"""


def main():
    """PSCP - Horizontal Histogram"""
    a_z = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    inp = input()
    state = False
    count = 0
    for i in a_z:
        if i in inp:
            count = inp.count(i)
            print(i+" : ",end="")
            for i in range(1,count+1):
                if state:
                    print("|",end="")
                    state = False
                elif not i % 5:
                    state =True
                print("-",end="")
            count = 0
            state = False
            print()

main()
