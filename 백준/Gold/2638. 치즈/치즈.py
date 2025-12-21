from collections import deque
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            cnt += 1
time = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
edge = [(0,y) for y in range(M)]+[(N-1,y) for y in range(M)]+[(x,0) for x in range(1,N-1)]+[(x,M-1) for x in range(1,N-1)]
while cnt:
    visited = [[False]*M for _ in range(N)]
    for x, y in edge:
        visited[x][y] = True
    count = [[0]*M for _ in range(N)]
    deq = deque(edge)
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny]==0:
                deq.append((nx,ny))
                visited[nx][ny] = True
            elif board[nx][ny]==1:
                count[nx][ny] += 1
    for x in range(N):
        for y in range(M):
            if count[x][y]>=2:
                board[x][y] = 0
                cnt -= 1
    time += 1
    if cnt == 0:
        break

print(time)