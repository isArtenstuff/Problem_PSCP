"""Giraffe"""

def main():
    """PSCP - Giraffe"""
    number = int(input())
    max_gi = 0
    count_notfull = 0
    index = 0
    first = 0
    last = 0
    giraffe = []
    if not number:
        print(0)
        return
    for _ in range(number):
        hight = int(input())
        if not hight:
            continue
        giraffe.append(hight)
    if len(giraffe) <= 2:
        print(1)
        return

    for i in giraffe:
        last += 1
        if not index:
            max_gi = i
            index += 1

        if first == 1 and max_gi < i:
            max_gi = i
            first = 0
            if last == number:
                count_notfull += 1
        elif max_gi > i and not first:
            count_notfull += 1

            first += 1
            max_gi = i
        elif i > max_gi:
            max_gi = i
            if last == number:
                count_notfull += 1
        else:
            max_gi = i
    print(count_notfull)

main()
