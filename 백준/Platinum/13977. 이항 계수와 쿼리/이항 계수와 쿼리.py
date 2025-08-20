MOD = 1_000_000_007
fact = list(range(4_000_000 + 1))
for i in range(2, 4_000_000 + 1):
    fact[i] = fact[i] * fact[i-1] % MOD

def power(base, exp, p): # base^exp mod p
    res = 1
    base %= p
    while exp > 0:
        if exp % 2 == 1:
            res = (res*base) % p
        base = (base*base) % p
        exp //= 2
    return res

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    fact_n = fact[N]
    fact_k = fact[K]
    fact_nk = fact[N-K]
    inv_k = power(fact_k, MOD-2, MOD)
    inv_nk = power(fact_nk, MOD-2, MOD)
    res = (fact_n * inv_k) % MOD
    res = (res * inv_nk) % MOD 
    print(res if res>0 else 1)
