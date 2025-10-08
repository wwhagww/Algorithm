import sys; input=sys.stdin.readline
N = int(input())
plst = list(map(int, input().split()))
if N == 1:
    print(0)
    exit(0)
adj = [[] for _ in range(N)]
for u, p in enumerate(plst[1:], start=1):
    adj[p].append(u)

dp = [0 for _ in range(N)]
def dfs(u):
    if not adj[u]: return
    for v in adj[u]:
        dfs(v)
    adj[u].sort(key=lambda x:-dp[x])
    dp[u] = max([dp[v]+i for i, v in enumerate(adj[u], start=1)])
dfs(0)
print(dp[0])