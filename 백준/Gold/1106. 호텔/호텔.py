G, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]
cities.sort(key=lambda x: -x[1]/x[0])

MAX_COST = (G//cities[0][1]+1) * cities[0][0] + 1
dp = [0] * MAX_COST

res = None
for cost, value in cities:
    for i in range(MAX_COST):
        dp[i] = max(dp[i], dp[i-cost]+value if i>=cost else 0)
        if dp[i] >= G: 
            res = i
            break
print(res)