# 어두운 길 > 전력난


def find(x):
    if par[x] != x:
        par[x] = find(par[x])
    return par[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: par[b] = a
    else: par[a] = b

while True:
    N, M = map(int, input().split())
    if N == 0:
        break
    data = []
    par = [i for i in range(N)]
    for _ in range(M):
        a, b, dist = map(int, input().split())
        data.append((dist, a, b))
    data.sort()
    res = 0
    for dist, a, b in data:
        if find(a) != find(b):
            union(a, b)
        else:
            res += dist
    print(res)
            