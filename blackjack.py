"""BlackJack"""

def main():
    """BlackJack Game."""
    total_card = int(input())
    cards = []
    scores = 0
    total_ace = 0

    for _ in range(total_card):
        pai = input()
        cards.append(pai)

    for card in cards:
        if card == "A":
            scores += 11
            total_ace += 1
        elif card in "JQK":
            scores += 10
        else: scores += int(card)

    while scores > 21 and total_ace:
        scores -= 10
        total_ace -= 1

    print(scores)

main()
