n, m = map(int, input().split())
graph = [[] for _ in range(n)]
indegree = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    graph[a].append(b)
    indegree[b] += 1

order = []
q = [idx for idx, cnt in enumerate(indegree) if cnt == 0]
while q:
    cur = q.pop()
    order.append(cur)
    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)
print(" ".join(map(lambda x: str(x+1), order)))