import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**5)
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

disc = [-1]*(V+1)
time = 0
edges_cut = []

def dfs(cur, p):
    global time
    disc[cur] = low = time
    time += 1
    for nxt in graph[cur]:
        if nxt == p: continue
        if disc[nxt] != -1:
            low = min(low, disc[nxt])
        else:
            low_nxt = dfs(nxt, cur)
            if low_nxt > disc[cur]:
                edges_cut.append((cur, nxt) if cur < nxt else (nxt, cur))
            low = min(low, low_nxt)
    return low
dfs(1, None)

print(len(edges_cut))
for a, b in sorted(edges_cut):
    print(a,b)