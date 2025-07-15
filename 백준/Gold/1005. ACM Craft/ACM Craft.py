from collections import deque
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    lst = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    indeg = [0] * (N+1)
    time = [0] * (N+1)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indeg[b] += 1
    goal = int(input())
    deq = deque([i for i in range(1, N+1) if indeg[i]==0])
    while deq:
        now = deq.popleft()
        t = time[now]+lst[now]
        if now == goal:
            print(t)
            break
        for next in graph[now]:
            indeg[next] -= 1
            time[next] = max(time[next], t)
            if indeg[next]==0:
                deq.append(next)
    