from heapq import heappop, heappush
INF = int(1e9)
cnt = 0
while True:
    N = int(input())
    if N == 0: break
    else: cnt += 1
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))

    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    table = [[INF]*N for _ in range(N)]
    table[0][0] = data[0][0]
    q = [(data[0][0], 0, 0)] # 거리, 행, 열
    while q:
        dist, x, y = heappop(q)
        if table[x][y] < dist: continue
        if x == N-1 and y == N-1:
            print(f'Problem {cnt}: {dist}')
            break
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                ndist = dist+data[nx][ny]
                if ndist < table[nx][ny]:
                    table[nx][ny] = ndist
                    heappush(q, (ndist, nx, ny))