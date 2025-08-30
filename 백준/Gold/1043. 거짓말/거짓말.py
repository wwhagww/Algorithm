from collections import deque
N, M = map(int, input().split())
_, *known = map(int, input().split())
is_known = [False]*N
for k in known:
    is_known[k-1] = True

que = set()
parties = []
go_list = [[] for _ in range(N)]
for i in range(M):
    _, *party = map(int, input().split())
    parties.append(list(map(lambda x:x-1 ,party)))
    for p in party:
        if is_known[p-1]: que.add(i)
        go_list[p-1].append(i)

# 파티 사이의 그래프로 생각. 단지 nxt를 고를때 2단계
visited = [False]*M
que = list(que)
for i in que:
    visited[i] = True

que = deque(que)
while que:
    cur = que.popleft()
    for p in parties[cur]:
        if is_known[p]: continue
        is_known[p] = True
        for nxt in go_list[p]:
            if visited[nxt]: continue
            visited[nxt] = True
            que.append(nxt)
print(visited.count(False))