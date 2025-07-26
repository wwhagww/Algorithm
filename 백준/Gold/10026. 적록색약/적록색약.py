#635
from collections import deque
N = int(input())
board = [input() for _ in range(N)]

dx = (-1,1,0,0)
dy = (0,0,-1,1)

visited = [[False]*N for _ in range(N)]
cnt = 0
for x in range(N):
    for y in range(N):
        if visited[x][y]: continue
        cnt += 1

        cur = board[x][y]

        deq = deque()
        deq.append((x, y))
        visited[x][y] = True

        while deq:
            cx, cy = deq.popleft()
            for i in range(4):
                nx, ny = cx+dx[i], cy+dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if visited[nx][ny]:
                    continue
                if board[nx][ny] == cur:
                    deq.append((nx, ny))
                    visited[nx][ny] = True
print(cnt, end=" ")

visited = [[False]*N for _ in range(N)]
cnt = 0        
for x in range(N):
    for y in range(N):
        if visited[x][y]: continue
        cnt += 1

        cur = board[x][y]

        deq = deque()
        deq.append((x, y))
        visited[x][y] = True

        while deq:
            cx, cy = deq.popleft()
            for i in range(4):
                nx, ny = cx+dx[i], cy+dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if visited[nx][ny]:
                    continue
                if (board[nx][ny]=="B") == (cur=="B"):
                    deq.append((nx, ny))
                    visited[nx][ny] = True
print(cnt)