"""Fibonacci Recursion V1"""


def main(n):
    """PSCP - Fibonacci Recursion V1"""
    if not n:
        return 0
    if n == 1:
        return 1
    return main(n - 1) + main(n - 2)

N = int(input())
print(main(N))
