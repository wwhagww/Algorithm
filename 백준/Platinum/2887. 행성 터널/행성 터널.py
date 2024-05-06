# 행성 터널
def find(par, x):
    if par[x] != x:
        par[x] = find(par, par[x])
    return par[x]

def union(par, a, b):
    a = find(par, a)
    b = find(par, b)
    if a < b: par[b] = a
    else: par[a] = b

N = int(input())

data = [[],[],[]]
for idx in range(N):
    line = list(map(int, input().split()))
    for i in range(3):
        data[i].append((line[i], idx))

edges = []
for lst in data:
    lst.sort()
    for i in range(N-1):
        edges.append((abs(lst[i+1][0] - lst[i][0]), lst[i][1], lst[i+1][1]))

edges.sort()
par = [i for i in range(N)]
res = 0
cnt = 0
for edge in edges:
    dist, a, b = edge
    if find(par, a) == find(par, b): continue
    union(par, a, b)
    res += dist
    cnt += 1
    if cnt == N-1:
        break
print(res)