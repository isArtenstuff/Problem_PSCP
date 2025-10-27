"""Paper"""

def main():
    """PSCP - Paper"""
    pap_1 = input()
    pap_2 = input()

    size_1 = int(pap_1[1:])
    size_2 = int(pap_2[1:])

    print(2 ** (size_2-size_1))

main()
