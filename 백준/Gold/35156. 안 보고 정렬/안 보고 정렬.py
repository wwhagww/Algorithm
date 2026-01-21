import sys; input = sys.stdin.readline

MOD = 998244353
def pow(a,n,m=MOD): # a의 n승
    res = 1
    while n > 0:
        if n % 2 == 1:
            res *= a
            res %= m
        a **= 2
        a %= m
        n //= 2
    return res % m

T = int(input())
for _ in range(T):
    N, L, R = map(int, input().split())
    k = R-L+1
    if k == 1:
        print(1)
    elif k == 2:
        result = pow(k,N) - 2
        while result < 0:
            result += MOD
        result %= MOD
        print(result)
    else:
        k %= MOD
        result = pow(k,N) - 2*pow(k-1,N) + pow(k-2,N)
        while result < 0:
            result += MOD
        result %= MOD
        print(result)