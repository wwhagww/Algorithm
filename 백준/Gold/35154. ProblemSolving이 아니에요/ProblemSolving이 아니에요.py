T = int(input())
N = 5001
MOD = 998244353
dp = [[0]*N for _ in range(N)]
"""
DP 정의
N*N DP
A개까지 고려했을때, 스택에 B개 남아있는 경우의 수

전이
[A][B] = [A-1][B+1] + [A-2][B-1] 인가..?

확인
[0][0] = 1
[1][0] = 0

[2][0] = 0  [2][1] = 1
[3][0] = 1  [3][1] = 0  [3][2] = 0
[4][0] = 0  [4][1] = 0  [4][2] = 1
[5][0] = 0  [5][1] = 2  [5][3] = 0
맞는 듯?
예제 테스트 해보자
"""
dp[0][0] = 1
for a in range(2, N):
    for b in range(a//2+1): # B 상한은 A//2
        dp[a][b] = (dp[a-1][b+1] + (dp[a-2][b-1] if b>=1 else 0)) % MOD

inp = map(int, input().split())
for a in inp:
    if a == 1: 
        print(-1)
        continue
    res = 0
    for b in range(a//2+1):
        res += dp[a][b]
        res %= MOD
    print(res)
