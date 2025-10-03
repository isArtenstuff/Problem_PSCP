"""Run Length Encoding"""
word = input()
AVOID = "/"
COUNT = 1
for index, i in enumerate(word):
    if i == AVOID:
        COUNT += 1
    elif i != AVOID and index:
        print(f"{COUNT}{AVOID}", end="")
        COUNT = 1
    AVOID = i
print(f"{COUNT}{AVOID}")
