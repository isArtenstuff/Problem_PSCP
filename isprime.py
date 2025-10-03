"""Is Prime Large"""
def prime(number):
    """ To check is this number prime """
    if number <= 1:
        return "NO"
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return "NO"
    return "YES"

print(prime(int(input())))
