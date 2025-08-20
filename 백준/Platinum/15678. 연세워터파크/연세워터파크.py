# 15678 연세워터파크
from collections import deque
N, D = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0]*N

deq = deque() # (idx, value)

for i in range(N):
    while deq and deq[0][0] < i - D:
        deq.popleft()
    prev_mx = deq[0][1] if deq else 0
    dp[i] = arr[i] + max(0, prev_mx)
    while deq and deq[-1][1] <= dp[i]:
        deq.pop()
    deq.append((i, dp[i]))
print(max(dp))