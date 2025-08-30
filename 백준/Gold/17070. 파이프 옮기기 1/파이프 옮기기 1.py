N = int(input())
board = []
for _ in range(N):
    board.append(input().split())

WALL = "1"
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
# 가로 0 대각 1 세로 2
dp[0][1][0] = 1
# 첫 줄 채우기
for c in range(2, N):
    if board[0][c] == WALL: break
    dp[0][c][0] = 1

for r in range(1, N):
    for c in range(1, N):
        if board[r][c] == WALL: 
            continue
        dp[r][c][0] = sum(dp[r][c-1][:2])
        dp[r][c][2] = sum(dp[r-1][c][1:])
        if board[r-1][c] == WALL or board[r][c-1] == WALL:
            continue
        dp[r][c][1] = sum(dp[r-1][c-1])
# print(*dp, sep="\n")
print(sum(dp[-1][-1]))