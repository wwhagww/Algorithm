import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**5)
N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    adj[u].append(v)

id_ = [0]
ids = [-1]*N
low = [0]*N
on_stack = [False]*N
stack = []

comp = []

def dfs(u):
    ids[u] = low[u] = id_[0]; id_[0] += 1
    stack.append(u); on_stack[u] = True

    for v in adj[u]:
        if ids[v] == -1:
            dfs(v)
        if on_stack[v]:
            low[u] = min(low[u], low[v])
    if low[u] == ids[u]:
        c = []
        while stack:
            x = stack.pop(); on_stack[x] = False
            c.append(x+1)
            if x == u: break
        c.sort()
        c.append(-1)
        comp.append(c)

for u in range(N):
    if ids[u] != -1: continue
    dfs(u)
comp.sort()

print(len(comp))
for c in comp:
    print(*c)