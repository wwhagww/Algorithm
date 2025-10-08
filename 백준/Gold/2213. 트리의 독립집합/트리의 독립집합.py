import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**4)
N = int(input())
wlst = list(map(int, input().split()))
adj = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    adj[u].append(v)
    adj[v].append(u)

dp = [[0, 0] for _ in range(N)]
dct = {}
def dfs(u, p):
    for v in adj[u]:
        if v == p: continue
        dfs(v, u)
        if dp[v][0] > dp[v][1]:
            dct[(u, v)] = 0
            dp[u][0] += dp[v][0]
        else:
            dct[(u, v)] = 1
            dp[u][0] += dp[v][1]
        dp[u][1] += dp[v][0]
    dp[u][1] += wlst[u]
dfs(0, -1)
res = []
def dfs2(u, p, stat):
    if stat == 1:
        res.append(u)
        for v in adj[u]:
            if v == p: continue
            dfs2(v, u, 0)
    else:
        for v in adj[u]:
            if v == p: continue
            dfs2(v, u, dct[(u, v)])
if dp[0][0] > dp[0][1]:
    print(dp[0][0])
    dfs2(0, -1, 0)
    res.sort()
    print(*map(lambda x: x+1, res))
else:
    print(dp[0][1])
    dfs2(0, -1, 1)
    res.sort()
    print(*map(lambda x: x+1, res))