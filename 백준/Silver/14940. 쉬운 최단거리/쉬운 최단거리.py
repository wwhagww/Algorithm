from collections import deque
N, M = map(int, input().split())
data = []
for i in range(N):
    data.append(line:=input().split())
    if "2" in line: st = (i, line.index("2"))
q = deque([(st[0], st[1], 0)]) # 좌표, 거리
table = [[-1]*M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while q:
    x, y, dist = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if data[nx][ny] == "1" and table[nx][ny] == -1:
                table[nx][ny] = dist+1
                q.append((nx, ny, dist+1))
for i in range(N):
    for j in range(M):
        if data[i][j] in "02": table[i][j] = 0
for line in table:
    print(" ".join(list(map(str, line))))
            