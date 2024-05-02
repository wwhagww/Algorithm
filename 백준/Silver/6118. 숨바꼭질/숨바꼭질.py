#숨바꼭질
from heapq import heappop, heappush
INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

table = [INF]*N
table[0] = 0
q = [(0, 0)] # 거리, 노드
while q:
    dist, i = heappop(q)
    if table[i] < dist: continue
    for ni in graph[i]:
        if dist+1 < table[ni]:
            table[ni] = dist+1
            heappush(q, (dist+1, ni))
val = max(table)
idx = table.index(val)+1
cnt = table.count(val)
print(idx, val, cnt)