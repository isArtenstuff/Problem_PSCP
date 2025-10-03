"""squid game (tug-of-war)"""
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
a7 = int(input())
a8 = int(input())
a9 = int(input())
a10 = int(input())
b1 = int(input())
b2 = int(input())
b3 = int(input())
b4 = int(input())
b5 = int(input())
b6 = int(input())
b7 = int(input())
b8 = int(input())
b9 = int(input())
b10 = int(input())
def who_die():
    """Who"""
    force_a = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
    force_b = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10
    if force_a > force_b :
        print("B")
    elif force_a < force_b :
        print("A")
    elif force_a == force_b :
        print("AB")
who_die()
