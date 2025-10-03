"""Elo"""
ra = int(input())
rb = int(input())
who = input()
Ea =  1 / (1 + (10 ** ((rb - ra) / 400)))
Eb =  1 / (1 + (10 ** ((ra - rb) / 400)))
if who == "A" :
    print(f"{Ea:.2f}")
elif who == "B" :
    print(f"{Eb:.2f}")
