"""One For All"""

number = int(input())
LAST_END = number
WORDS = ""
INDEX = 0
while number > 0:
    name_hero = input()
    if not INDEX:
        WORDS += name_hero
        INDEX += 1
    elif not INDEX % 2:
        WORDS += ("-"*(INDEX)+name_hero)
        INDEX += 1
    else:
        WORDS += ("*"*(INDEX)+name_hero)
        INDEX += 1
    if INDEX == LAST_END:
        WORDS += "_"+str(LAST_END)
    number -= 1
print(WORDS)
