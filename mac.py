"""MAC NA JA"""


def is_valid_mac(mac):
    """docstring"""
    text1 = "ABCDEFabcdef"
    text2 = "0123456789"

    if len(mac) == 17:
        LOC = mac[2]
        if LOC not in "-:":
            return "ERROR"
        for i in range(0, 17):
            if not (i + 1) % 3:
                if mac[i] != LOC:
                    return "ERROR"
            elif mac[i] not in text1 + text2:
                return "ERROR"
        return {"-": "VALID 1", ":": "VALID 2"}[LOC]

    if len(mac) == 14:
        LOC = mac[4]
        if LOC != ".":
            return "ERROR"
        for i in range(0, 14):
            if not (i + 1) % 5:
                if mac[i] != ".":
                    return "ERROR"
            elif mac[i] not in text1 + text2:
                return "ERROR"
        return "VALID 3"
    return "ERROR"


def main():
    """docstring"""
    macAddress = input()
    result = is_valid_mac(macAddress)
    print(result)

main()
