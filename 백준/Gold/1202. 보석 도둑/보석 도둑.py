import heapq

N, K = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

gems.sort()
bags.sort() 

res = 0
heap = []
i = 0
for bag in bags:
    while i < N and gems[i][0] <= bag:
        heapq.heappush(heap, -gems[i][1])
        i += 1
    if heap:
        res += -heapq.heappop(heap)
print(res)