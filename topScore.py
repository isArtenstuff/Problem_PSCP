"""Top score"""
stu = int(input())
def total_top() :
    """find top score and total"""
    most_sco = 0
    top = 0
    for _ in range (stu) :
        sco = int(input())
        if most_sco < sco:
            most_sco = sco
            top = 1
        elif sco == most_sco :
            top += 1
    print(most_sco)
    print(top)
total_top()
