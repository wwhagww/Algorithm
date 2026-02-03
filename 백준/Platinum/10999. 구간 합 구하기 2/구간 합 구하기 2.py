import sys; input = sys.stdin.readline
nn,M,K = map(int, input().split())
arr = []
for _ in range(nn):
    arr.append(int(input()))

N = 1
H = 0
while N < nn:
    N <<= 1
    H += 1

lazy = [0]*N
tree = [0]*(2*N)
sz = [0]*(2*N)

for i in range(N):
    tree[i+N] = arr[i] if i < nn else 0
    sz[i+N] = 1

for i in range(N-1, 0, -1):
    tree[i] = tree[i<<1] + tree[i<<1 | 1]
    sz[i] = sz[i<<1] * 2

def apply(cur, v):
    tree[cur] += v * sz[cur]
    if cur < N:
        lazy[cur] += v

def build(cur):
    while cur > 1:
        cur >>= 1
        tree[cur] = tree[cur<<1] + tree[cur<<1|1] + lazy[cur]*sz[cur]

def update(l,r,v):
    l += N; r += N
    l0,r0 = l,r
    while l <= r:
        if l % 2 == 1:
            apply(l, v)
            l += 1
        if r % 2 == 0:
            apply(r, v)
            r -= 1
        l >>= 1; r >>= 1
    # 빌드
    build(l0); build(r0)

def push(cur):
    for shift in range(H, 0, -1):
        i = cur >> shift
        if lazy[i] != 0:
            apply(i<<1, lazy[i])
            apply(i<<1 | 1, lazy[i])
            lazy[i] = 0

def query(l,r):
    # 푸쉬
    l+=N;r+=N
    push(l); push(r)

    res = 0
    while l <= r:
        if l % 2 == 1:
            res += tree[l]
            l += 1
        if r % 2 == 0:
            res += tree[r]
            r -= 1
        l >>= 1; r >>= 1
    return res

for _ in range(M+K):
    a, b, c, *d = map(int, input().split())
    b-=1; c-=1
    if a == 1: # 변경
        update(b, c, d[0])
    else: # 쿼리
        print(query(b,c))