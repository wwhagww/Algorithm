import sys; input=sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    node, *neigh = map(int, input().split())
    for i in range(0,len(neigh)-1,2):
        graph[node].append((neigh[i], neigh[i+1]))
graph[1].append((0,0))
max_width = 0

depths = [0]*(N+1)
stack = [(1, 0, 0)] # node, parent, dist_parent
while stack:
    # print(stack)
    cur, p, dp = stack.pop()
    if len(graph[cur]) == 1: # 리프 노드
        max_width = max(max_width, depths[p]+dp)
        depths[p] = max(depths[p], dp) 
        # 리프 바로 위 노드 뎁쓰 갱신
        continue

    if depths[cur] == 0: # 첫 방문
        stack.append((cur, p, dp))
        for child, d in graph[cur]:
            if child == p: continue
            stack.append((child, cur, d))
        continue

    max_width = max(max_width, depths[p] + dp+depths[cur])
    depths[p] = max(depths[p], dp+depths[cur])

print(max_width)