"""Finding mix colors"""
color1 = input().strip().lower()
color2 = input().strip().lower()
primary_colors = {"red", "yellow", "blue"}
if color1 not in primary_colors or color2 not in primary_colors:
    print("Error")
elif color1 == color2:
    print(color1.capitalize())
else:
    mix = {color1, color2}
    if mix == {"red", "yellow"}:
        print("Orange")
    elif mix == {"red", "blue"}:
        print("Violet")
    elif mix == {"yellow", "blue"}:
        print("Green")
    else:
        print("Error")
