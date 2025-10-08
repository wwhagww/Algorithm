import sys; input=sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
edges= []
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1
    if v < u: u, v = v, u
    edges.append((w, u, v, i))

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1]*n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return False
        if self.sz[a] < self.sz[b]: a,b = b,a
        self.p[b] = a
        self.sz[a] += self.sz[b]
        return True

res = [2]*M
dsu = DSU(N)
edges.sort(reverse=True)

while edges:
    w = edges[-1][0]
    adj = [[] for _ in range(N)]
    nodes = set()
    unions = set()
    while edges and w == edges[-1][0]:
        _, u, v, i = edges.pop()
        a, b = dsu.find(u), dsu.find(v)
        if a == b:
            res[i] = "3"
        else:
            unions.add((a, b))
            adj[a].append((b, i))
            adj[b].append((a, i))
            nodes.add(a); nodes.add(b)

    disc = [-1]*N
    low = [0]*N
    time = [0]

    def dfs(u, peid):
        disc[u] = low[u] = time[0]; time[0] += 1
        for v, eid in adj[u]:
            if eid == peid: continue
            if disc[v] == -1:
                dfs(v, eid)
                if low[v] > disc[u]:
                    res[eid] = "1"
                low[u] = min(low[u], low[v])
            else:
                low[u] = min(low[u], disc[v])
    
    for root in nodes:
        if disc[root] != -1: continue
        dfs(root, -1)

    for a, b in unions:
        dsu.union(a, b)

print(*res, sep="\n")