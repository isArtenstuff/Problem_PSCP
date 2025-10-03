"""GCD_N"""
import math
N = int(input())
gcd_result = int(input())
for i in range(N - 1) :
    tor = int(input())
    gcd_result = math.gcd(gcd_result, tor)
    i += i
print(gcd_result)
