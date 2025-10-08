import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**4)
while True:
    N = int(input())
    if N == 0: break
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        adj[u].append((v,w))
        adj[v].append((u,w))

    subsz = [0]*N
    dp = [0]*N
    def dfs(u, p):
        for v, w in adj[u]:
            if v == p: continue
            dfs(v, u)
            subsz[u] += subsz[v]
            dp[u] += subsz[v] * w + dp[v]
        subsz[u] += 1
    dfs(0, -1)

    dp2 = [0]*N
    dp2[0] = dp[0]
    def dfs2(u, p):
        for v, w in adj[u]:
            if v == p: continue
            dp2[v] = dp2[u] + w * (N - 2 * subsz[v])
            dfs2(v, u)
    dfs2(0, -1)
    print(min(dp2))
