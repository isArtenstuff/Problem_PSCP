"""This program's to find min day to exercise"""
import math
push = int(input())
sit = int(input())
squ = int(input())
run = int(input())
push_day = int(input())
sit_day = int(input())
run_day = int(input())
squ_day = int(input())

def day():
    """Finding min day"""
    day_done = 0
    push_count = math.ceil(push / push_day)
    sit_count = math.ceil(sit / sit_day)
    squ_count = math.ceil(squ / squ_day)
    run_count = math.ceil(run / run_day)
    if push_count > day_done :
        day_done = push_count
    if sit_count > day_done :
        day_done = sit_count
    if squ_count > day_done :
        day_done = squ_count
    if run_count > day_done :
        day_done = run_count
    print(day_done)
day()
