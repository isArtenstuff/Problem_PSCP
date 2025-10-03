"""Pich Them"""
import json
number = json.loads(str(input()))
even = []
for i in number:
    if not i % 2 :
        even.append(i)
for i in even:
    print(i)
if not even:
    print("Nope")
