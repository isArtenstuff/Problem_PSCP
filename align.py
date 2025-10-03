"""Align"""
all_place_take = int(input())
place = input()
word = input()

space_size = all_place_take - len(word)

if place == "left":
    print(word, end="")
    print(" " * space_size)
elif place == "right":
    print(" " * space_size, end="")
    print(word)
elif place == "center":
    if space_size % 2:
        FOR_LEFT = space_size - (space_size // 2)
        FOR_RIGHT = space_size // 2
        print(" " * FOR_LEFT, end="")
        print(word, end="")
        print(" " * FOR_RIGHT)
    else:
        FOR_TWO_SIDE = int(space_size / 2)
        print(" " * FOR_TWO_SIDE, end="")
        print(word, end="")
        print(" " * FOR_TWO_SIDE)
