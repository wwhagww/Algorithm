# 스티커
# 다이나믹
T = int(input())
for _ in range(T):
    N = int(input())
    data = []
    data.append(list(map(int, input().split())))
    data.append(list(map(int, input().split())))
    
    if N == 1:
        print(max(data[0][0], data[1][0]))
        continue
    
    dp = [[0]*N, [0]*N]
    dp[0][0] = data[0][0]
    dp[0][1] = data[1][0]+data[0][1]
    dp[1][0] = data[1][0]
    dp[1][1] = data[0][0]+data[1][1]
    
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + data[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + data[1][i]
    
    print(max(dp[0][-1], dp[1][-1]))