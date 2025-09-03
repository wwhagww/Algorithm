from collections import deque
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input().rstrip())

mx = 0

def idx(c):
    return ord(c) - ord("A")
def next(r, c):
    return [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
que = deque([(0, 0, 1, 1<<idx(board[0][0])), ]) # r, c, cnt, visited
while que:
    # print(que)
    r, c, cnt, visited = que.pop()
    # print(r, c, cnt, bin(visited))
    mx = max(cnt, mx)
    for nr, nc in next(r, c):
        if not (0 <= nr < N and 0 <= nc < M): continue
        if visited & 1<<idx(board[nr][nc]): continue
        que.append((nr, nc, cnt+1, visited | 1<<idx(board[nr][nc])))
    
print(mx)