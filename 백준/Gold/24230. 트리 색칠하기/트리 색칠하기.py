n = int(input())
colors = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    graph[a].append(b)
    graph[b].append(a)

stack = [(0,0)] # (노드번호, 부모노드 색깔)
count = 0
visited = set()
while stack:
    current, parrentColor = stack.pop()
    if current in visited: continue # 기우?
    else: visited.add(current)
    if colors[current] != parrentColor:
        count += 1
    for node in graph[current]:
        if node in visited: continue
        stack.append((node, colors[current]))
print(count)