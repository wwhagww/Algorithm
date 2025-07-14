from collections import deque
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indeg = [0] * (N+1)

for _ in range(M):
    ln, *lst = map(int, input().split())
    for i in range(ln-1):
        graph[lst[i]].append(lst[i+1])
        indeg[lst[i+1]] += 1

deq = deque([i for i in range(1, N+1) if indeg[i]==0])
res = []
while deq:
    now = deq.popleft()
    res.append(now)
    for next in graph[now]:
        indeg[next] -= 1
        if indeg[next] == 0:
            deq.append(next)
if len(res) == N:
    for r in res: print(r)
else: print(0)