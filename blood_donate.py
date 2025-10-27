"""Blood Donation"""

def main():
    """PSCP - Blood Donation"""
    age = int(input())
    weight = int(input())
    donet = int(input())
    approve = None
    error = 0

    if age < 17 or age > 70:
        error += 1
    if weight >= 45:
        pass
    else:
        error += 1

    if (not donet and age <= 55) or donet > 0:
        pass
    else:
        error += 1

    if age == 17 or 60 <= age <= 70:
        approve = input()
        if approve == "True":
            pass
        else:
            error += 1

    if error > 0:
        print("No")
    else:
        print("Yes")

main()
