import math
N = int(input())
arr = []
for _ in range(N):
    arr.append(input())
K = int(input())

rem_10 = []
rem = 1
for _ in range(750):
    rem %= K
    rem_10.append(rem)
    rem *= 10

arr_len = []
arr_num = []
for num in arr:
    arr_len.append(len(num))
    arr_num.append(int(num)%K)

dp = [[0]*K for _ in range(1<<N)]

for idx in range(1<<N):
    # print(f"idx {idx:03b}")
    sum_len = 0
    for i in range(N):
        if (idx & 1<<i):
            sum_len += arr_len[i]
    for i in range(N):
        if not (idx & 1<<i): continue
        ln = sum_len - arr_len[i]
        if ln == 0:
            dp[idx][arr_num[i]] = 1
            continue
        for rem, cnt in enumerate(dp[idx & ~(1<<i)]):
            dp[idx][(rem + arr_num[i]*rem_10[ln]) % K] += cnt
        
# a / b
a = dp[-1][0]
b = math.factorial(N)

gcd = math.gcd(a, b)
a //= gcd
b //= gcd
print(f"{a}/{b}")
