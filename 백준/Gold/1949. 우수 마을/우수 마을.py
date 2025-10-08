import sys; input=sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input())
town = list(map(int, input().split()))
adj = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    adj[u].append(v)
    adj[v].append(u)

dp = [[0, 0] for _ in range(N)]

def dfs(u, p):
    for v in adj[u]:
        if v == p: continue
        dfs(v, u)
        dp[u][1] += dp[v][0]
        dp[u][0] += max(dp[v][1], dp[v][0])
    dp[u][1] += town[u]
dfs(0, -1)
print(max(dp[0]))