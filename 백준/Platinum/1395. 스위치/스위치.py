import sys; input = sys.stdin.readline
n, M = map(int, input().split())
N = 1
H = 0
while N < n:
    N <<= 1
    H += 1
tree = [0] * (2*N)
lazy = [0] * N
sz = [0] * (2*N)
for i in range(n):
    sz[i+N] = 1
for i in range(N-1, 0, -1):
    sz[i] = sz[i<<1] + sz[i<<1|1]

# print(sz)

def apply(p, v):
    if v:
        tree[p] = sz[p] - tree[p]
    if p < N:
        lazy[p] ^= v

def build(p):
    while p > 1:
        p >>= 1
        if lazy[p]:
            tree[p] = sz[p]-(tree[p<<1] + tree[p<<1|1]) 
        else:
            tree[p] = (tree[p<<1] + tree[p<<1|1])
def push(p):
    for s in range(H, 0, -1):
        i = p >> s
        if lazy[i] == 0: continue
        apply(i<<1, lazy[i])
        apply(i<<1|1, lazy[i])
        lazy[i] = 0

for _ in range(M):
    o, l, r = map(int, input().split())
    l-=1; r-=1
    l += N; r += N
    if o == 0:
        # 구간 갱신
        l0, r0 = l, r
        while l <= r:
            if l & 1:
                apply(l, 1)
                l += 1
            if not(r&1):
                apply(r, 1)
                r -= 1
            l >>= 1; r >>= 1
        build(l0); build(r0)

    else:
        # 구간 쿼리
        push(l); push(r)
        res = 0
        while l <= r:
            if l & 1:
                res += tree[l]
                l += 1
            if not(r&1):
                res += tree[r]
                r -= 1
            l >>= 1; r >>= 1
        print(res)
