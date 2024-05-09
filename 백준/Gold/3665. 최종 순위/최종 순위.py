# 최종 순위 3665
from collections import deque
T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    
    tmp = [[False]*(N+1) for _ in range(N+1)]
    for i in range(N):
        a = data[i]
        for b in data[i+1:]:
            tmp[a][b] = True
            
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        tmp[a][b], tmp[b][a] = tmp[b][a], tmp[a][b]
        
    graph = [[] for _ in range(N+1)]
    ind = [0]*(N+1)
    for a in range(1, N+1):
        for b in range(1, N+1):
            if tmp[a][b]:
                graph[a].append(b)
                ind[b] += 1
    # print("#", graph)
    
    q = deque()
    res = []
    
    chk = False
    cnt = 0
    for i in range(1, N+1):
        if ind[i] == 0:
            q.append(i)
            cnt += 1
    if cnt > 1: chk = True
    
    while q:
        now = q.popleft()
        res.append(now)
        
        cnt = 0
        for i in graph[now]:
            ind[i] -= 1
            if ind[i] == 0:
                q.append(i)
                cnt += 1
        if cnt > 1: chk = True
    
    # print("#", res)
    if len(res) < N:
        print("IMPOSSIBLE")
    elif chk:
        print("?")
    else:
        print(" ".join(map(str, res)))
    
    