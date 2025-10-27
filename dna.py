"""docstring"""


def main():
    """docstring"""
    first_dna = input()
    sec_dna = input()
    text = ""
    dna_output = ""
    chack = first_dna + sec_dna
    chack = chack.replace("A","")
    chack = chack.replace("C","")
    chack = chack.replace("G","")
    chack = chack.replace("T","")
    if len(chack) > 0:
        print("Error")
        return

    for i in first_dna:
        text += i
        #print(text)
        if text in sec_dna:
            if len(text) > len(dna_output):
                dna_output = text
        else:
            text = text[1:]
    if not dna_output:
        print("None")
    else:
        print(dna_output)

main()
