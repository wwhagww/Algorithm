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

N = int(input())
M = int(input())
graph = [{} for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split())
    if (b-1 in graph[a-1]) and (graph[a-1][b-1] < w):
        continue
    graph[a-1][b-1] = w


st, ed = map(int, input().split())
dist = dijkstra(graph, st-1)
print(dist[ed-1])