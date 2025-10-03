"""Word Sequence I"""
word = input()
size = len(word)
for col in range(size):
    for row in range(col + 1):
        print(word[row], end="")
    print()
