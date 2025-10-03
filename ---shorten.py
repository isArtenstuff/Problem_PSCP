"""Shorten"""
alll = []
output = ""
while True:
    n = int(input())   
    if n == -1:
        break
    alll.append(n)
    for i in alll:
        if i == n:
            print(i)