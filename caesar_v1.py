"""Caesar V1"""

shift = int(input())
words = input()
OUTPUT = ""
for char in words:
    if char.isalpha():
        if char.islower():
            OUTPUT += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            OUTPUT += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        OUTPUT += char
print(OUTPUT)
