from collections import deque
N, M = map(int, input().split())
board = []
for i in range(N):
    line = list(input())
    for j in range(M):
        if line[j] == "R": 
            rx,ry = i, j
            line[j] = "."
        elif line[j] == "B":
            bx, by = i, j
            line[j] = "."
    board.append(line)

def move_one(x, y, dx, dy):
    dist = 0
    while board[x+dx][y+dy] != "#":
        x, y = x+dx, y+dy
        dist += 1
        if board[x][y] == "O": break
    return x, y, dist
                    
dx = [1,-1,0,0]
dy = [0,0,1,-1]
deq = deque([(rx,ry,bx,by, 0), ])
while deq:
    rx,ry,bx,by, cnt = deq.popleft()
    
    if board[rx][ry] == "O":
        print(cnt)
        break
    for i in range(4):
        nrx, nry, rdist = move_one(rx,ry,dx[i],dy[i])
        nbx, nby, bdist = move_one(bx,by,dx[i],dy[i])
        if board[nbx][nby] == "O": continue
        if nrx == nbx and nry == nby:
            if rdist > bdist:
                nrx, nry = nrx-dx[i], nry-dy[i]
            else:
                nbx, nby = nbx-dx[i], nby-dy[i]
        if cnt < 10:
            deq.append((nrx, nry, nbx, nby, cnt+1))
else:
    print(-1)