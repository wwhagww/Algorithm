# 플로이드
n = int(input())
m = int(input())
dp = [[1e9]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a-1][b-1] = min(dp[a-1][b-1], c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
for i in range(n):
    for j in range(n):
        if dp[i][j] == 1e9: dp[i][j] = 0
for line in dp:
    print(" ".join(map(str, line)))