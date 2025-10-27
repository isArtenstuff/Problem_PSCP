"""Lucky Number"""
def main():
    """PSCP - Lucky Number"""
    n = int(input())
    number = list(range(1, n + 1))
    number = [x for i, x in enumerate(number) if (i + 1) % 2]
    index = 1

    while index < len(number):
        step = number[index]
        if step > len(number):
            break
        new_numbers = []
        for i, num in enumerate(number):
            if (i + 1) % step:
                new_numbers.append(num)

        number = new_numbers
        index += 1

    print(" ".join(map(str, number)))

main()
