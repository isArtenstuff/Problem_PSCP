"""Count Vowel"""
n = int(input())
count = 0
for _ in range(n):
    vowel = input() 
    if vowel in "AEIOU" :
        count += 1
print(count)
