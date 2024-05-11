# 청소년 상어 19236

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


res = []
def dfs(acc, board, dir, sx, sy):
    tg, board[sx][sy] = board[sx][sy], 0
    dir[0] = dir[tg]
    acc += tg
    
    # print(acc, sx, sy)
    # print("\n".join(str(board)[2:-2].split("], [")))
    
    pos = [False]*17
    for x in range(4):
        for y in range(4):
            if board[x][y]:
                pos[board[x][y]] = (x, y)
    for i in range(1,17):
        if pos[i] == False: continue
        x, y = pos[i]
        while True:
            nx, ny = x+dx[dir[i]], y+dy[dir[i]]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy):
                pos[i], pos[board[nx][ny]] = pos[board[nx][ny]], pos[i]
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                break
            else:
                dir[i] = dir[i] % 8 + 1
    
    cand = []
    while True:
        sx += dx[dir[0]]
        sy += dy[dir[0]]
        if 0 <= sx < 4 and 0 <= sy < 4:
            if board[sx][sy] > 0:
                cand.append((sx, sy))
        else: break
    
    if cand:
        for x, y in cand:
            dfs(acc, [line[:] for line in board], dir[:], x, y)
    else:
        res.append(acc)

board = []
dir = [0]*17
for _ in range(4):
    line = list(map(int, input().split()))
    board.append([line[i] for i in range(0,8,2)])
    for i in range(0,8,2):
        dir[line[i]] = line[i+1]
    
dfs(0, [line for line in board], dir[:], 0, 0)
print(max(res))