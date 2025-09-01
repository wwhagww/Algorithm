from collections import deque
import sys; input=sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

idx = [None]*N
for i, n in enumerate(A):
    if n == 0: continue
    idx[n-1] = i

tree = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    tree[a].append(b)
    tree[b].append(a)

deq = deque([(0, 0)]) # 최소 인덱스, 노드
lst = [] # 적어도 이 인덱스 이후에 들어가야함
visited = [False]*N
while deq:
    p, node = deq.popleft()
    visited[node] = True
    if idx[node] is None:
        lst.append(p)
    else: # 고정점
        p = max(p, idx[node])
    deq.extend([(p, child) for child in tree[node] if not visited[child]])
    # 큐로 bfs 순회하므로 부모 체크할 필요 없음

lst.sort(reverse=True)

res = 1
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
