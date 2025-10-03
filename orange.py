"""Oranges"""
def sell_orange() :
    """Oranges"""
    o_level = int(input())
    o_sell = int(input())
    remain_level = o_level
    for i in range(1, o_level + 1) :
        total = i * i
        if o_sell >= total :
            o_sell -= total
            remain_level -= 1
        else :
            break
    print(remain_level)
sell_orange()
