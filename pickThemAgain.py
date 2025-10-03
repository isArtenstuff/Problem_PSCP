"""Pick Them Again"""
number = input().split(" ")
three_five = []
for I in number:
    I = int(I)
    if not I % 3 or not I % 5:
        three_five.append(I)
if len(three_five) > 0:
    for I in range(len(three_five) - 1, -1, -1):
        print(three_five[I])
else:
    print("Nope")
