"""KABATA"""
total_line = int(input())
KEEP = {}
def is_kabata(sentence:str):
    """is it in kabata language"""
    if "baka" in sentence:
        return "no"
    if "bakka" in sentence:
        sentence = sentence.replace("bakka", "")
    if "ba" in sentence:
        sentence = sentence.replace("ba", "")
    if "ka" in sentence:
        sentence = sentence.replace("ka", "")
    if "ta" in sentence:
        sentence = sentence.replace("ta", "")

    if sentence:
        return "no"
    return "yes"

for i in range(total_line):
    SEN = str(input())
    KEEP[f"{i}"] = is_kabata(SEN)

for i in KEEP.values():
    print(i)
