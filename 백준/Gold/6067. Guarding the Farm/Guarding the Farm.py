from collections import deque
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

isVisited = [[False]*m for _ in range(n)]

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

countSummit = 0
for i in range(n):
    for j in range(m):
        if isVisited[i][j]: continue

        currentVisited = set([(i, j)])
        isSummit = True
        height = board[i][j]

        deq = deque([(i,j)])
        while deq:
            ci, cj = deq.popleft()
            for idx in range(8):
                ni = ci + di[idx]
                nj = cj + dj[idx]
                if not (0 <= ni < n and 0 <= nj < m): continue
                if board[ni][nj] > height:
                    isSummit = False
                elif board[ni][nj] == height and (ni, nj) not in currentVisited:
                    deq.append((ni, nj))
                    currentVisited.add((ni, nj))
        for vi, vj in list(currentVisited):
            isVisited[vi][vj] = True
        if isSummit: countSummit += 1
print(countSummit)