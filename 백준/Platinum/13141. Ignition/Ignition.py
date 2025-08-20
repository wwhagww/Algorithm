# 13141 이그니션
N, M = map(int, input().split())
INF = float("inf")
D = [[INF]*N for _ in range(N)]
edges = []
for node in range(N):
    D[node][node] = 0
for _ in range(M):
    a, b, dist = map(int, input().split())
    a, b = a-1, b-1
    D[a][b] = min(D[a][b], dist)
    D[b][a] = min(D[b][a], dist)
    edges.append((a, b, dist))
# print("\n".join(list(map(str, D))))
# print(edges)

for m in range(N):
    for s in range(N):
        for e in range(N):
            D[s][e] = min(D[s][e], D[s][m]+D[m][e])

t_min = INF
for node in range(N):
    t = 0
    for a, b, dist in edges:
        t = max(t, D[node][a]+D[node][b]+dist)
    t_min = min(t_min, t)
# print("\n".join(list(map(str, D))))
print(t_min/2)