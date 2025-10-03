"""Christmas Light"""
COLOR = input()
total_light = int(input())
if COLOR == "R" :
    COLOR = "Red"
elif COLOR == "G" :
    COLOR = "Green"
if COLOR == "B" :
    COLOR = "Blue"
def main() :
    """Red Green Blue"""
    result = ""
    now = COLOR
    for _ in range(total_light) :
        result += now + " "
        if now in ("R", "Red"):
            now = "Green"
        elif now in ("G", "Green"):
            now = "Blue"
        elif now in ("B", "Blue"):
            now = "Red"
    print(result)
main()
