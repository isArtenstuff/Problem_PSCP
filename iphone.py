"""Iphone 13"""

def main():
    """PSCP - Iphone 13"""
    gen = input()
    mem = input()
    i13_mini = {"128 GB" : 25900, "256 GB" : 29900, "512 GB" : 37900}
    i13 = {"128 GB" : 29900, "256 GB" : 33900, "512 GB" : 41900}
    i13_pro = {"128 GB" : 38900, "256 GB" : 42900, "512 GB" : 50900, "1 TB" : 58900}
    i13_promax = {"128 GB" : 42900, "256 GB" : 46900, "512 GB" : 54900, "1 TB" : 62900}
    
    if gen == "IPhone 13 mini":
        print(i13_mini[mem])
    elif gen == "IPhone 13":
        print(i13[mem])
    elif gen == "IPhone 13 Pro":
        print(i13_pro[mem])
    elif gen == "IPhone 13 Pro Max":
        print(i13_promax[mem])

main()
