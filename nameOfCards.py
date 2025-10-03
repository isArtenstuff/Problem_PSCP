"""Name of Cards"""
name = input().upper()
GROUP = name[-1]
CARD = name.replace(name[-1], "")

match GROUP:
    case "C" :
        GROUP = "Clubs"
    case "D" :
        GROUP = "Diamonds"
    case "H" :
        GROUP = "Hearts"
    case "S" :
        GROUP = "Spades"
match CARD:
    case "A" :
        CARD = "Ace"
    case "J" :
        CARD = "Jack"
    case "Q" :
        CARD = "Queen"
    case "K" :
        CARD = "King"
print(f"{CARD} of {GROUP}")
