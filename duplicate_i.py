"""Duplicate I"""

def main():
    """PSCP - Duplicate I"""
    m = int(input())
    n = int(input())
    current = True
    index = 0
    group_1 = []
    group_2 = []
    for i in range(m + n):
        number = int(input())
        if current:
            group_1.append(number)
            index += 1
            if index == m:
                current = False
        else:
            group_2.append(number)

    sus = list(set(group_1) & set(group_2))
    if not sus:
        print("Nope")
    else:
        sus.sort(reverse=True)
        for i in sus:
            print(i)

main()
