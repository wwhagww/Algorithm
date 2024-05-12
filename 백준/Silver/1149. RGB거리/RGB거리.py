N = int(input())
data = [[], [], []]
for _ in range(N):
    r, g, b = map(int, input().split())
    data[0].append(r)
    data[1].append(g)
    data[2].append(b)
dp = [[0]*N for _ in range(3)]
for c in range(3):
    dp[c][0] = data[c][0]
for i in range(1, N):
    for c in range(3):
        dp[c][i] = min([dp[c2][i-1] for c2 in range(3) if c2 != c]) + data[c][i]
print(min(dp[0][-1], dp[1][-1], dp[2][-1]))