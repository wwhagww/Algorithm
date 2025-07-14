G, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]

MAX_COST = 100 * 1000 + 1
dp = [0] * MAX_COST

res = None
for cost, value in cities:
    for i in range(MAX_COST):
        dp[i] = max(dp[i], dp[i-cost]+value if i>=cost else 0)
        if dp[i] >= G: 
            res = i
            break
print(res)