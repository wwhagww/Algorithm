s = input()
lens = len(s)
dp = [1]
NUM = 20000303
for i in range(10**6//8):
    dp.append(dp[-1] * 10**8 % NUM)
res = 0
for i, cur in enumerate(range(lens-8, -1, -8)):
    res += int(s[cur:cur+8]) * dp[i] % NUM
    res %= NUM
else:
    if cur > 0:
        res += int(s[:cur]) * dp[i+1] % NUM
        res %= NUM
print(res)