from collections import deque
N = int(input())
A = list(map(lambda x: int(x), input().split()))

idx = [None]*N
for i, n in enumerate(A):
    if n == 0: continue
    idx[n-1] = i

res = 1

tree = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    tree[a].append(b)
    tree[b].append(a)

pos = [0]*N # 적어도 이 인덱스 이후에 들어가야함
deq = deque([(0, 0)]) # 최소 인덱스, 노드
lst = []
visited = set()
while deq:
    p, node = deq.popleft()
    visited.add(node)
    if idx[node] is None:
        pos[node] = p
        lst.append(p)
    else: # 고정점
        p = max(p, idx[node])
    deq.extend([(p, child) for child in tree[node] if child not in visited])

lst.sort(reverse=True)

cnt_zero = 0
prev = N
for p in lst:
    cnt_zero += A[p:prev].count(0)
    prev = p
    if cnt_zero == 0: 
        res = 0
        break
    res *= cnt_zero
    res %= (10**9+7)
    cnt_zero -= 1

print(res % (10**9+7))
