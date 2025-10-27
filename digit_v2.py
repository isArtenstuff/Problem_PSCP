"""Digit V2"""


def main():
    """PSCP - Digit V2"""
    text = input()
    newt = text.split()
    num_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90
}
    if text == "zero":
        print(1)
        return
    if "thousand" in text:
        print(4)
    elif "hundred" in text:
        print(3)
    elif num_dict[str(newt[0])]:
        print(len(str(num_dict[str(newt[0])])))

main()
