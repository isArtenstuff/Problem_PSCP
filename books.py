"""Books"""
import math

def main():
    """PSCP - Books"""
    books = int(input())
    total_pages = int(input())
    x = int(input())
    y = int(input())

    if not books:
        print(0)
        return
    readpage = 0
    day = 0
    book = 0
    i = 0
    state = False
    while book < books:
        day += 1
        readpage += math.ceil((x+i)/(y+i) * total_pages)
        # print(readpage, day, i, book)
        if state:
            day = (books - book) + day - 1
            break
        if readpage >= total_pages:
            if readpage == total_pages:
                state = True
            book += 1
            readpage = 0
        i += 1
    print(day)

main()
