T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0]+list(map(int, input().split()))
    indeg = [0]*(n+1)
    for g in graph:
        indeg[g] += 1
    cnt = 0
    stack = [g for g in range(n+1) if indeg[g]==0]
    while stack:
        now = stack.pop()
        cnt += 1
        next = graph[now]
        indeg[next] -= 1
        if indeg[next] == 0:
            stack.append(next)
    print(cnt)