# 어두운 길 > 전력난
import sys
input = sys.stdin.readline
def find(par, x):
    if par[x] != x:
        par[x] = find(par, par[x])
    return par[x]

def union(par, a, b):
    a = find(par, a)
    b = find(par, b)
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
        if find(par, a) != find(par, b):
            union(par, a, b)
        else:
            res += dist
    print(res)