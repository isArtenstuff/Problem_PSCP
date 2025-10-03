"""GCD_2"""
a = int(input())
b = int(input())
def gcd(most, result):
    """Use Euclidean to find GCD"""
    while result:
        most, result = result, most % result
    return abs(most)
if a > b:
    print(gcd(a, b))
else:
    print(gcd(b, a))
