"""Century"""
total = int(input())
for i in range(total):
    year_type, year_num = input().split()
    year_num = int(year_num)
    if year_type == "B.E.":
        year_num = year_num - 543
        if year_num > 0:
            if year_num % 100:
                print(year_num // 100 + 1)
            else :
                print(year_num // 100)
        else :
            print("ERROR")
    elif year_type == "A.D.":
        if year_num > 0:
            if year_num % 100:
                print(year_num // 100 + 1)
            else :
                print(year_num // 100)
        else :
            print("ERROR")
    else :
        print("ERROR")
    i += i
