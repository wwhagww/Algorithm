import sys; input=sys.stdin.readline
N = int(input())
dp_max = [[0]*3 for _ in range(N)]
dp_min = [[0]*3 for _ in range(N)]
dp_max[0] = list(map(int, input().split()))
dp_min[0] = dp_max[0][:]
for i in range(1, N):
    a, b, c = map(int, input().split())
    dp_max[i][0] = max(dp_max[i-1][:2]) + a
    dp_max[i][1] = max(dp_max[i-1]) + b
    dp_max[i][2] = max(dp_max[i-1][1:]) + c
    dp_min[i][0] = min(dp_min[i-1][:2]) + a
    dp_min[i][1] = min(dp_min[i-1]) + b
    dp_min[i][2] = min(dp_min[i-1][1:]) + c
print(max(dp_max[-1]), min(dp_min[-1]))