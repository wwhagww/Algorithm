from collections import defaultdict
n = int(input())
board = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)

dp = [[set(line[:j]) for j in range(n)] for line in board]
# for i in range(1, n):
#     for j in range(n):
#         dp[i][j].update(dp[i-1][j])
#         dp[i][j].add(board[i-1][j])

maxVal = -1
for i in range(n):
    for j in range(n):
        v = board[i][j]
        if v <= maxVal: continue
        if v in dp[i][j]: 
            maxVal = v
            continue
        for ii in range(i):
            if v in dp[ii][j] or v == board[ii][j]:
                maxVal = v
                break
print(maxVal)
