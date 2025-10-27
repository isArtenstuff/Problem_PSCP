"""Ramen Bowl"""


def main():
    """PSCP - Ramen bowl"""
    plate = int(input())
    stack = []
    count = []
    for _ in range(plate):
        number = int(input())
        stack.append(number)
    for i in stack:
        count.append(stack.count(i))
    print(max(count))

main()
