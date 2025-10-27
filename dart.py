"""Dart"""

def main():
    """PSCP - Dart"""
    n = int(input())
    scores = 0

    for _ in range(n):
        x, y = map(int, input().split())
        place_take = x * x + y * y

        if place_take <= 4:
            scores += 5
        elif place_take <= 16:
            scores += 4
        elif place_take <= 36:
            scores += 3
        elif place_take <= 64:
            scores += 2
        elif place_take <= 100:
            scores += 1

    print(scores)

main()
