from collections import deque
N ,K = map(int, input().split())
adj = [[] for _ in range(N)]
parent = [None]*N
for _ in range(N-1):
    p, c = map(int, input().split())
    adj[p].append(c)
    parent[c] = p
apple = list(map(int, input().split()))
cnt = 0
que = deque([(0,0),]) # node, dist
while que:
    cur, d = que.popleft()
    if apple[cur] == 1: cnt += 1
    if d == K: continue
    for nxt in adj[cur]:
        if parent[cur] == nxt: continue
        que.append((nxt,d+1))
print(cnt)
