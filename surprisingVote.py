"""Surprising Vote"""
score = float(input())
maxx = float(input())
score = score - maxx
def surpri():
    """Is it's surprise"""
    if score >= maxx:
        return score - maxx
    return 0
noi = surpri()
if maxx - noi > 2:
    print("Surprising")
else:
    print("Not surprising")
