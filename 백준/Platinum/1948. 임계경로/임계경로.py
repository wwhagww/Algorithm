import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
rev   = [[] for _ in range(N+1)]
indeg = [0]*(N+1)

for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    rev[b].append((a, w))
    indeg[b] += 1

ST, ED = map(int, input().split())

dist = [-1]*(N+1)
dist[ST] = 0
q = deque([ST])

while q:
    cur = q.popleft()
    for nxt, w in graph[cur]:
        if dist[cur] + w > dist[nxt]:
            dist[nxt] = dist[cur] + w
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            q.append(nxt)

cnt = 0
vis = [False]*(N+1)
dq = deque([ED])
vis[ED] = True

while dq:
    cur = dq.popleft()
    for prev, w in rev[cur]:
        if dist[prev] + w == dist[cur]:  # 임계 간선
            cnt += 1
            if not vis[prev]:
                vis[prev] = True
                dq.append(prev)

print(dist[ED])
print(cnt)
