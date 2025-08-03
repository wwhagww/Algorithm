import sys; read = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N)]
nei = [0]*N
nei[0] += 1

for _ in range(N-1):
    a,b,dist = map(int,read().split())
    a, b = a-1, b-1
    graph[a].append((b,dist))
    graph[b].append((a,dist))
    nei[a] += 1
    nei[b] += 1

paths = [None]*N
paths[0] = ()
dists = [0]*N
ancs = [0]*N

que = [(0, None)]
while que:
    cur, prev = que.pop()
    for idx, (nxt,d) in enumerate(graph[cur]):
        if nxt == prev: continue
        ancs[nxt] = ancs[cur] if nei[cur] <= 2 else cur
        dists[nxt] = dists[cur] + d
        paths[nxt] = paths[cur] if nei[cur] <= 2 else paths[cur]+(idx,)
        que.append((nxt, cur))

M = int(input())
for _ in range(M):
    a, b = map(int, read().split())
    a, b = a-1, b-1
    pa, pb = paths[a], paths[b]
    la, lb = len(pa), len(pb)
    ml = min(la, lb)
    
    for i in range(ml):
        if pa[i] != pb[i]:
            idx = i
            break
    else: idx = ml
    
    if ml==idx:
        res = abs(dists[a]-dists[b])
    else:
        tmp = a if la == ml else b
        for _ in range(ml-idx):
            tmp = ancs[tmp]
        res = dists[a] + dists[b] - 2*dists[tmp]
    print(res)
