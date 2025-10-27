"""Line Sorting"""

def main():
    """PSCP - Line Sorting"""
    number = int(input())
    words_sort = []
    for _ in range(number):
        text = input()
        words_sort.append(text)

    words_sort = sorted(words_sort, key=len)

    for i in words_sort:
        print(i)

main()
