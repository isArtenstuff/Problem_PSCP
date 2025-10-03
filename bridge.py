"""bridge"""
a = int(input())
b = int(input())
goal = int(input())
def bridge() :
    """how many a have to use in bridge"""
    max_big = goal // 5
    use_big = min(b, max_big)
    remaining = goal - (use_big * 5)
    if remaining <= a:
        print(remaining)
    else:
        print(-1)
bridge()
