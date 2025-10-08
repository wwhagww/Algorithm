import sys; input=sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    adj[u].append(v)
    adj[v].append(u)

dp = [[0, 0] for _ in range(N)]
stack = [(0, -1, 0)]
while stack:
    u, p, phs = stack.pop()
    if phs == 0:
        stack.append((u, p, 1))
        for v in adj[u]:
            if v == p: continue
            stack.append((v, u, 0))
    else:
        for v in adj[u]:
            if v == p: continue
            dp[u][1] += min(dp[v])
            dp[u][0] += dp[v][1]
        dp[u][1] += 1
print(min(dp[0]))