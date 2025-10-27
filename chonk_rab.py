"""Chonk Rabbit"""

def main():
    """Chonk Rabbit"""
    l = int(input())
    count_rab = 0
    wid = []
    o = 0
    hon = ""
    newname = ""
    maxn = 0
    for _ in range(l):
        name = input()
        wid.append(name)
    for i in wid:
        hon = i
        o = int(hon.split()[-1])
        if o > 15:
            count_rab += 1
        if o > maxn:
            maxn = o
            newname = hon
    print(count_rab)
    print(newname)

main()
