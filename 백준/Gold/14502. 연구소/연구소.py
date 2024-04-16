from collections import deque
from itertools import combinations
n, m = map(int, input().split())
virus = []
space = []
board = []
for i in range(n):
    line = input().split()
    for j in range(m):
        if line[j] == "2": virus.append((i,j))
        if line[j] == "0": space.append((i,j))
    board.append(line)
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
mx = 0
for comb in combinations(space, 3):
    board_t = [line[:] for line in board]
    deq = deque(virus)
    for i, j in comb:
        board_t[i][j] = "1"
    while deq:
        i, j = deq.popleft()
        board_t[i][j] = "2"
        for idx in range(4):
            ni, nj = i+di[idx], j+dj[idx]
            if 0 <= ni < n and 0 <= nj < m and board_t[ni][nj] == "0":
                deq.append((ni, nj))
    cnt = 0
    for line in board_t:
        for cell in line:
            if cell == "0": cnt += 1
    if cnt > mx: mx = cnt
print(mx)