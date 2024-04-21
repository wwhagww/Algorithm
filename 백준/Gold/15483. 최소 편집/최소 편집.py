a = input()
b = input()
la = len(a)
lb = len(b)
dp = [[0]*(lb+1) for _ in range(la+1)]
for i in range(la+1): dp[i][0] = i
for i in range(lb+1): dp[0][i] = i
for ia in range(1, la+1):
    for ib in range(1, lb+1):
        if a[ia-1] == b[ib-1]:
            dp[ia][ib] = dp[ia-1][ib-1]
        else:
            dp[ia][ib] = 1 + min(dp[ia-1][ib-1], dp[ia-1][ib], dp[ia][ib-1])
print(dp[-1][-1])