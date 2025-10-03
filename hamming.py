"""Hamming"""
inp_1 = input()
inp_2 = input()
COUNT = 0
LONG = len(inp_1)
for i in range(LONG):
    if inp_1[i] != inp_2[i]:
        COUNT += 1
print(COUNT)
