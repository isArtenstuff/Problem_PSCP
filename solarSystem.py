"""Solar System"""

def main():
    """PSCP - Solar System"""
    solar = input()+" "
    first,last,now = "","",""
    hot,cool = "",""
    sun_hear = False
    first_space,last_space = -1,0
    # Loop Through the space!
    for letter in solar:
        if letter == " ":
            if not sun_hear:
                first_space += 1
            else:
                last_space += 1
            if not first:
                first = now
            if last == "Sun":
                hot += now
            if now == "Sun":
                sun_hear = True
                hot += last+" "
            last = now
            now = ""
            continue
        now += letter
    # Checking for Cool planets!
    if first != "Sun" and first not in hot and first_space>=last_space:
        cool += first+" "
    if last != "Sun" and last not in hot and last_space>=first_space:
        cool += last+" "
    if solar.strip().count(" ") <= 2 and first_space==last_space:
        print("Hot:",hot.lstrip().rstrip())
        print("Cool:",hot.lstrip().rstrip())
        return
    if solar.strip().count(" ") < 2:
        print("Hot:",hot.lstrip().rstrip())
        print("Cool:",hot.lstrip().rstrip())
        return
    print("Hot:",hot.lstrip().rstrip())
    print("Cool:",cool.lstrip().rstrip())

main()
