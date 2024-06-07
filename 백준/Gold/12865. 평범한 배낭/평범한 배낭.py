# 평범한 배낭
N, M = map(int, input().split())
dp = [[0]*(M+1) for _ in range(N+1)]
weights = []
values = []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
for i in range(1, N+1):
    for w in range(1, M+1):
        if w >= weights[i-1]:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
        else:
            dp[i][w] = dp[i-1][w]
# print("\n".join(str(dp)[2:-2].split("], [")))
print(dp[N][M])