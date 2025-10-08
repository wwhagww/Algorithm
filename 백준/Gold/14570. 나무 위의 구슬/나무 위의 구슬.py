import sys; input=sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N)]
for u in range(N):
    a, b = map(int, input().split())
    if a != -1: adj[u].append(a-1)
    if b != -1: adj[u].append(b-1)
K = int(input())

stack = [(0, K)]
while stack:
    u, k = stack.pop()
    ln = len(adj[u])
    if ln == 0:
        print(u+1)
    elif ln == 1:
        stack.append((adj[u][0], k))
    else:
        if k % 2 == 1:
            stack.append((adj[u][0], k // 2 + 1))
        else:
            stack.append((adj[u][1], k // 2))