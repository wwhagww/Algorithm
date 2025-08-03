import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
LOG = 17  # 2^17 > 40000
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [0]*(N+1)
parent = [[0]*(LOG+1) for _ in range(N+1)]

stack = [(1, 0)]
while stack:
    cur, p = stack.pop()
    for nxt in graph[cur]:
        if nxt == p: continue
        depth[nxt] = depth[cur] + 1
        parent[nxt][0] = cur
        stack.append((nxt, cur))

for k in range(1, LOG+1):
    for i in range(1, N+1):
        parent[i][k] = parent[parent[i][k-1]][k-1]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    for k in reversed(range(LOG+1)):
        if depth[u] - (1<<k) >= depth[v]:
            u = parent[u][k]
    if u == v:
        return u
    for k in reversed(range(LOG+1)):
        if parent[u][k] != parent[v][k]:
            u = parent[u][k]
            v = parent[v][k]
    return parent[u][0]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    anc = lca(a, b)
    print(anc)
