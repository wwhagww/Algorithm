import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

max_width = 0

def dfs(node):
    global max_width
    depths = [dfs(child)+dist for child, dist in graph[node]]
    if not depths:
        return 0
    depths.sort(reverse=True)
    width = depths[0]
    if len(depths) >= 2:
        width += depths[1]
    max_width = max(max_width, width)
    return depths[0]

dfs(1)

print(max_width)