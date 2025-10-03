"""Overlapping"""
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())
def over():
    """Is overlapping"""
    distance_squared = (x1 - x2)**2 + (y1 - y2)**2
    sum_radii = r1 + r2
    if distance_squared <= sum_radii**2:
        print("overlapping")
    else:
        print("no overlapping")
over()
