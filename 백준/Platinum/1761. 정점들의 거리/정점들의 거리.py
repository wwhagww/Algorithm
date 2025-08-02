import sys; read = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N)]
nei = [0]*N
for _ in range(N-1):
    a,b,dist = map(int,read().split())
    a, b = a-1, b-1
    graph[a].append((b,dist))
    graph[b].append((a,dist))
    nei[a] += 1
    nei[b] += 1

# print(graph)
# print(nei)

paths = [None]*N
dists = [None]*N # from root
pars = [None]*N # parent have not only one child

root = 0
paths[root] = ()
dists[root] = 0
pars[root] = 0
nei[root] += 1

que = [(0, None)]
while que:
    cur, nochild = que.pop()
    for idx, (child,d) in enumerate(graph[cur]):
        if child == nochild: continue
        # update pars
        pars[child] = pars[cur] if nei[cur] <= 2 else cur
        # update dists
        dists[child] = dists[cur] + d
        # update paths
        paths[child] = paths[cur] if nei[cur] <= 2 else paths[cur]+(idx,)

        que.append((child, cur))

# print(paths)
# print(dists)
# print(pars)

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
            tmp = pars[tmp]
        res = dists[a] + dists[b] - 2*dists[tmp]
    print(res)
