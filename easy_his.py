"""Easy Histogram"""


def main():
    """PSCP - Easy Histogram"""
    a_z = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    sumco = 0
    words_added = []
    text = input()
    for i in a_z:
        if i in text:
            for j in text:
                if i == j:
                    sumco += 1
            words_added.append(f"{i} = {sumco}")
            sumco = 0
    for i in words_added:
        print(i)

main()
