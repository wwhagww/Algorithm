import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**4)

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

disc = [-1]*(V+1)
low = [-1]*(V+1)
is_cut = [False] * (V+1)
time = 0

def dfs(cur, p):
    global time
    disc[cur] = low[cur] = time
    time += 1  
    child = 0

    for nxt in graph[cur]:
        if nxt == p: continue
        if disc[nxt] == -1: # 첫 방문
            child += 1
            dfs(nxt, cur)
            low[cur] = min(low[cur], low[nxt])
            if p is not None and low[nxt] >= disc[cur]:
                is_cut[cur]  = True
        else:
            low[cur] = min(low[cur], disc[nxt])
    if p is None and child > 1:
        is_cut[cur] = True

for root in range(1, V+1):
    if disc[root] != -1: continue
    dfs(root, None)

res = [i for i, cut in enumerate(is_cut) if cut]
print(len(res))
if res:
    print(*sorted(res))
