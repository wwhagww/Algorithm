from bisect import bisect_left
N, K = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

gems.sort(key=lambda x: -x[1])
bags.sort()

visit = [0]*K
res = 0
for weight, value in gems:
    idx = bisect_left(bags, weight)
    if idx >= K: continue
    while visit[idx] != 0:
        visit[idx] += 1
        idx += visit[idx]-1
        if idx >= K: break
    else:
        visit[idx] += 1
        res += value
print(res)
