"""Calculator"""
def cal():
    """How many time have to push ?"""
    num_want = int(input())
    times = ""
    if num_want == 1:
        print(1)
    else:
        for i in range(1, num_want + 1):
            times += str(i) + "+"
        print(len(times))
cal()
