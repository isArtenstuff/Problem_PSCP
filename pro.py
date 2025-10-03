"""Pro"""
x = int(input())
y = int(input())
a = int(input())
z = int(input())
def total_buffet ():
    """Pro"""
    have_dis = z // x
    no_dis = z % x
    pay = (have_dis * y) + no_dis
    price = pay * a
    print(price)
total_buffet()
