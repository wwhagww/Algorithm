from collections import deque

N = int(input())
graph = list(map(lambda x: int(x)-1, input().split()))
goal = list(map(lambda x: int(x)-1, input().split()))

cnt = [0] * N
inv = [[] for _ in range(N)]

for i in range(N):
    cnt[graph[i]] += 1
    inv[graph[i]].append(i)

def swap(prev, cur):
    graph[prev] = graph[cur]
    graph[cur] = cur

    inv[graph[prev]].remove(cur)
    inv[graph[prev]].append(prev)

    inv[cur].remove(prev)
    inv[cur].append(cur)

ok = True

for cur in range(N):
    if graph[cur] == goal[cur]: continue
    if goal[cur] == cur: continue
    tmp = graph[cur]
    while tmp != goal[cur]:
        if graph[tmp] == tmp or goal[tmp] != tmp: 
            ok = False; break
        swap(cur, tmp)
        tmp = graph[cur]
    else: continue
    break
else:
    for cur in range(N):
        if graph[cur] == goal[cur]: continue
        if len(inv[cur]) == 0:
            ok = False; break

print("YES" if ok else "NO")