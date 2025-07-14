import sys
read = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [["0"]*N for _ in range(N)]

for i in range(N): dp[i][i] = "1"
for i in range(N-1): dp[i+1][i] = "1" if lst[i] == lst[i+1] else "0"

for i in range(2, N):
    for j in range(i-1):
        dp[i][j] = "1" if dp[i-1][j+1]=="1" and lst[i] == lst[j] else "0"

# for line in dp: print("".join(line))

M = int(read())
for _ in range(M):
    s, e = map(int, read().split())
    print(dp[e-1][s-1])