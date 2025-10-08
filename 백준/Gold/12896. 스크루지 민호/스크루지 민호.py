import sys; input=sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    adj[u].append(v)
    adj[v].append(u)

res = [0]
dp = [[0,0] for _ in range(N)]
def dfs(u, p):
    for v in adj[u]:
        if v == p: continue
        dfs(v, u)
        dpv = dp[v][0] + 1
        if dpv > dp[u][0]:
            dp[u] = [dpv, dp[u][0]]
        elif dpv > dp[u][1]:
            dp[u] = [dp[u][0], dpv]
    res[0] = max(res[0], dp[u][0]+dp[u][1])
dfs(0, -1)
print((res[0]+1)//2)