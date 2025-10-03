"""ball"""
def bounce() :
    """ball"""
    high_drop = float(input())
    count = 0
    while True :
        high_drop = high_drop * 3 / 5
        if high_drop < 0.01 :
            break
        count += 1
    print(count)
bounce()
