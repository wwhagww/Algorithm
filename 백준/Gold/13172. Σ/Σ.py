import sys; input=sys.stdin.readline
import math
MOD = 10**9+7
def power(base, exp, mod):
    if exp == 0: return 1
    res = 1
    while exp>0:
        if exp%2==1:
            res *= base
            res %= mod
        base *= base
        base &= mod
        exp //= 2
    return res
# a / b
N = int(input())
fb, fa = map(int, input().split())
for _ in range(N-1):
    b, a = map(int, input().split())
    fa = ((a*fb)%MOD + (fa*b)%MOD) % MOD
    fb =(fb*b)%MOD

print(fa * pow(fb, MOD-2, MOD) % MOD)