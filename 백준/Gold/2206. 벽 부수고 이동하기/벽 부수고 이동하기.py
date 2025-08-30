from collections import deque
N ,M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

WALL = "1"
que = deque([(0, 0, 1, True), ])
# r, c, step, power
visited_p = [[False]*M for _ in range(N)]
visited_np = [[False]*M for _ in range(N)]
visited_p[0][0] = True

def nxt(r, c):
    return [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]
while que:
    r, c, step, power = que.popleft()
    if r == N-1 and c == M-1:
        print(step)
        break
    for nr, nc in nxt(r, c):
        if not (0 <= nr < N and 0 <= nc < M): continue
        if power:
            if visited_p[nr][nc]: continue
            visited_p[nr][nc] = True
            visited_np[nr][nc] = True
        else:
            if visited_np[nr][nc]: continue
            visited_np[nr][nc] = True
        
        if board[nr][nc] != WALL:
            que.append((nr, nc, step+1, power))
        elif power:
            que.append((nr, nc, step+1, False))
else:
    print(-1)