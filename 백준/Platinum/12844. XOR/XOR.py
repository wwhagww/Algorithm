import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
M = int(input())

N = 1
H = 0
while N < n:
    N <<= 1
    H += 1
    
sz = [0] * (2*N)
tree = [0] * (2*N)
lazy = [0] * N

for i in range(n):
    sz[i+N] = 1
    tree[i+N] = arr[i]
for i in range(N-1, 0, -1):
    sz[i] = sz[i<<1] + sz[i<<1|1]
    tree[i] = tree[i<<1] ^ tree[i<<1|1]

def apply(p, v):
    if sz[p] & 1: tree[p] ^= v
    if p < N:
        lazy[p] ^= v

def build(p):
    while p > 1:
        p >>= 1
        tree[p] = tree[p<<1] ^ tree[p<<1|1]
        if sz[p]&1: tree[p] ^= lazy[p] 
def push(p):
    for s in range(H, 0, -1):
        i = p >> s
        if lazy[i] == 0: continue
        apply(i<<1, lazy[i])
        apply(i<<1|1, lazy[i])
        lazy[i] = 0

for _ in range(M):
    line = list(map(int, input().split()))
    s, e = line[1]+N, line[2]+N
    if line[0] == 1:
        # 구간 갱신
        k = line[3]
        s0, e0 = s, e
        while s <= e:
            if s & 1:
                apply(s, k)
                s += 1
            if not(e&1):
                apply(e, k)
                e -= 1
            s >>= 1; e >>= 1
        build(s0); build(e0)

    else:
        # 구간 쿼리
        push(s); push(e)
        res = 0
        while s <= e:
            if s & 1:
                res ^= tree[s]
                s += 1
            if not(e&1):
                res ^= tree[e]
                e -= 1
            s >>= 1; e >>= 1
        print(res)
