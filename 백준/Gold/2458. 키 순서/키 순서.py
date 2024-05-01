N, M = map(int, input().split())
table = [[False]*i + [True] + [False]*(N-i-1) for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    table[a-1][b-1] = True
for k in range(N):
    for i in range(N):
        for j in range(N):
            if table[i][k] and table[k][j]: table[i][j] = True
res = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if table[i][j]: cnt += 1
        if table[j][i]: cnt += 1
    if cnt > N: res += 1
print(res)