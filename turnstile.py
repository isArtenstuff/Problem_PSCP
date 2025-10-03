"""Turn Stiles"""
def turn():
    """Turn Stiles"""
    now = "Locked"
    count = 0
    while True:
        s = input()
        match s:
            case "P":
                if now == "Unlocked":
                    now = "Locked"
                    count += 1
                else:
                    continue
            case "C":
                if now == "Locked":
                    now = "Unlocked"
                else:
                    continue
            case "END":
                break
    print(count)
turn()
