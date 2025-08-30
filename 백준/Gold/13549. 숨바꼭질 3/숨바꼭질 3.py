S, G = map(int, input().split())
dp = [abs(S-i) for i in range(10**5+1)]
cur = S
while cur < G:
    if cur == 0:
        dp[1] = 1
        cur = 1
        continue
    for i in range(cur+1, cur*2+1):
        if i > G: break
        if i % 2 == 0:
            dp[i] = min(
                dp[cur]+abs(cur - i),
                dp[i//2]
                )
        else:
            dp[i] = min(
                dp[cur]+abs(cur-i), 
                dp[(i+1)//2] + 1,
                dp[(i-1)//2] + 1 
                )
    cur *= 2
print(dp[G])