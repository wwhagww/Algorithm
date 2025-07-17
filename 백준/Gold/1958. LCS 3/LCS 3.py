line_a = " "+input()
line_b = " "+input()
line_c = " "+input()
la = len(line_a)
lb = len(line_b)
lc = len(line_c)

dp = [[[0]*lc for _ in range(lb)] for _ in range(la)]

for i in range(1, la):
    a = line_a[i]
    for j in range(1, lb):
        b = line_b[j]
        for k in range(1, lc):
            c = line_c[k]
            if a == b == c:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])

print(dp[-1][-1][-1])