# 아기 상어 16236
from collections import deque
N = int(input())
data = []
for i in range(N):
    line = list(map(int, input().split()))
    if 9 in line:
        gx, gy = i, line.index(9)
    data.append(line)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

time = 0
size = 2
cnt = 0
while True:
    data[gx][gy] = 0
    
    chk = [[False]*N for _ in range(N)]
    chk[gx][gy] = True
    
    q = deque([(0, gx, gy)])
    cand = []
    
    while q:
        step, x, y = q.popleft()
        if cand and step > cand[0][0]:
            break
        if 0 < data[x][y] < size:
            cand.append((step, x, y))
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if data[nx][ny] <= size and not chk[nx][ny]:
                    q.append((step+1, nx, ny))
                    chk[nx][ny] = True
    
    if cand:
        cand.sort()
        step, x, y = cand[0]
        time += step
        gx, gy = x, y
        cnt += 1
        if cnt == size:
            cnt = 0
            size += 1
    else:
        break
print(time)