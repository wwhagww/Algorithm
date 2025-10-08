import sys; input=sys.stdin.readline
# sys.setrecursionlimit(10**5)
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        u -=1; v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    dp = [0]*N
    def dfs(u, p):
        for v, w in adj[u]:
            if v == p: continue
            if len(adj[v]) > 1: 
                dfs(v, u)
                dp[u] += min(w, dp[v])
            else:
                dp[u] += w
    dfs(0, -1)
    print(dp[0])