# 구간 합 구하기 5
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
data = [[0]*(N+1)]
for _ in range(N):
    data.append([0]+list(map(int, input().split())))
for x in range(1, N+1):
    for y in range(1, N+1):
        data[x][y] += data[x-1][y] + data[x][y-1] - data[x-1][y-1] 
# print("\n".join(str(data)[2:-2].split("], [")))
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(data[x2][y2] 
          - data[x1-1][y2] 
          - data[x2][y1-1] 
          + data[x1-1][y1-1])