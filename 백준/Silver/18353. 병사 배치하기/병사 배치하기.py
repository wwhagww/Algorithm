from bisect import bisect_left
n = int(input())
data = list(map(int, input().split()))
dp = [(0, 1e9), (1, data[0])]
for i in range(1, n):
    cur = data[i]
    for j in range(i, -1, -1):
        l, v = dp[j]
        if v > cur:
            dp.insert(bisect_left(dp, (l+1, cur)), (l+1, cur))
            break
print(n- dp[-1][0])