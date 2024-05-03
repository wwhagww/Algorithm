from heapq import heappush, heappop
V, E = map(int, input().split())
st = int(input())
INF = int(1e9)

graph = [{} for _ in range(V)]
for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1] if b-1 in graph[a-1] else INF)

table = [INF]*V
q = [(0, st-1)]
table[st-1] = 0
while q:
    d, i = heappop(q)
    if table[i] < d:
        continue
    for ni, nd in graph[i].items():
        if d+nd < table[ni]:
            table[ni] = d+nd
            heappush(q, (d+nd, ni))
for d in table:
    if d < INF:
        print(d)
    else:
        print("INF")