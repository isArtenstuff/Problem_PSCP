"""Heads and Legs"""
head = int(input())
legs = int(input())
bird = ((4 * head) - legs) // 2
rabbit = head - bird
if bird < 0 or rabbit < 0 or ((4 * head) - legs) % 2:
    print("Impossible")
else:
    print(rabbit, bird)
