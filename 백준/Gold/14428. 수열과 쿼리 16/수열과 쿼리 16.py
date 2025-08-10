import sys; input=sys.stdin.readline

N = int(input())
size = 1
while size < N: size <<= 1
A = list(map(int, input().split()))

INF = 10**9+1
tree = [(INF, INF)] * (2*size)

for i, v in enumerate(A):
    tree[size + i] = (v, i)

for i in reversed(range(1,size)):
    tree[i] = min(tree[i << 1], tree[i << 1 | 1])

M = int(input())
for _ in range(M):
    com, a, b = map(int, input().split())

    if com == 1: # 갱신
        i = a - 1
        p = size + i
        tree[p] = (b, i)
        p >>= 1
        while p:
            tree[p] = min(tree[p<<1], tree[p<<1 | 1])
            p >>= 1

    elif com == 2: # 쿼리
        l, r = (a-1) + size, (b-1) + size
        res = (INF, INF)
        while l <= r:
            if l & 1:
                res = min(res, tree[l])
                l += 1
            if not (r & 1):
                res = min(res, tree[r])
                r -= 1
            l >>= 1; r >>= 1
        print(res[1]+1)