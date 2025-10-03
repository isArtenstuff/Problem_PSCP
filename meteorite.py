"""Meteorite"""
weigh = float(input())
breakk = int(input())
save = float(input())
def count_missiles(a, b, c):
    """missiles"""
    if a < c:
        return 0
    return 1 + b * count_missiles(a / b, b, c)
print(count_missiles(weigh, breakk, save))
