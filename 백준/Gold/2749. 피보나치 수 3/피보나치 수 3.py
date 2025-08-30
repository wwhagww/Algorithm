def fib_mod(n, m):
    def _fdm(k):
        if k == 0:
            return (0, 1)
        a, b = _fdm(k >> 1)
        c = (a * ((2*b - a) % m)) % m
        d = (a*a + b*b) % m
        return (d, (c + d) % m) if (k & 1) else (c, d)
    return _fdm(n)[0]

N = int(input())
print(fib_mod(N, 1_000_000))