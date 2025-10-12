"""Paper"""
paper_1 = input()
paper_2 = input()
SIZE_1 = int(paper_1[1:])
SIZE_2 = int(paper_2[1:])
OUTPUT = 2 ** (SIZE_2 - SIZE_1)
print(OUTPUT)
