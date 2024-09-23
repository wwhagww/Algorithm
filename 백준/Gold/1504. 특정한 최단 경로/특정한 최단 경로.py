from heapq import heappush, heappop

def dijkstra(graph, start):
    # graph는 인접리스트 [{인접노드: 거리, ...}, ...]
    # start는 출발 노드
    # dist(거리 리스트) return
    INF = int(1e9)
    dist = [INF] * len(graph)
    dist[start] = 0

    visited = set()
    pq = [(0, start)] # (거리, 노드번호)
    while pq:
        cur_dist, cur_node = heappop(pq)
        if cur_node in visited: continue
        visited.add(cur_node)
        for neighbor, weight in graph[cur_node].items():
            new_dist = cur_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heappush(pq, (new_dist, neighbor))
    return dist

V, E = map(int, input().split())
graph = [{} for _ in range(V)]
for _ in range(E):
    a, b, w = map(int, input().split())
    a, b = a-1, b-1
    # if (b in graph[a]) and (graph[a][b] < w):
    #     continue
    graph[a][b] = w
    graph[b][a] = w


p1, p2 = map(int, input().split())
p1, p2 = p1-1, p2-1
dist_0 = dijkstra(graph, 0)
dist_p1 = dijkstra(graph, p1)
dist_p2 = dijkstra(graph, p2)
path1 = dist_0[p1] + dist_p1[p2] + dist_p2[V-1]
path2 = dist_0[p2] + dist_p2[p1] + dist_p1[V-1]
res = min(path1, path2)
if res >= int(1e9): res = -1
print(res)