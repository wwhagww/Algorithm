from collections import deque
N, M = map(int, input().split())
board = []
for i in range(N):
    line = list(input())
    board.append(line)
    for j in range(M):
        if line[j]=="I":
            pos = (i, j)

deq = deque([pos])
visited = [[False]*M for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

cnt = 0
while deq:
    x, y = deq.popleft()
    if visited[x][y]: continue
    visited[x][y] = True

    if board[x][y] == "P":
        cnt += 1

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if not visited[nx][ny] and board[nx][ny] != "X":
            deq.append((nx, ny))

print(cnt if cnt > 0 else "TT")