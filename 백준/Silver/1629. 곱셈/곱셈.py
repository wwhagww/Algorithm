# 곱셈
a, b, c = map(int, input().split())
bb = bin(b)[2:]
lb = len(bb)
dp = [0]*lb
dp[0] = a % c
for i in range(1, lb):
    dp[i] = dp[i-1] * dp[i-1] % c
res = 1
for i in range(len(bb)):
    if bb[lb-i-1] == "0": continue
    res *= dp[i]
    res %= c
print(res)