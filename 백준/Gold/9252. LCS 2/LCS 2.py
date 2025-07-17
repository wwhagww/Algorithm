line_a = " "+input()
line_b = " "+input()
N = len(line_a)
M = len(line_b)

dp = [[0]*M for _ in range(N)]

for r in range(1, N):
    a = line_a[r]
    for c in range(1, M):
        b = line_b[c]
        cand_up = dp[r-1][c]
        cand_left = dp[r][c-1]
        if a == b:
            if cand_up == dp[r-1][c-1]: 
                cand_up += 1
            if cand_left == dp[r-1][c-1]: 
                cand_left += 1

        dp[r][c] = max(cand_left, cand_up)

# for line in dp: print("".join(map(str, line)))

lcs = []
r, c = N-1 , M-1
while dp[r][c] > 0:
    if dp[r][c] == dp[r][c-1]:
        c -= 1
    elif dp[r][c] == dp[r-1][c]:
        r -= 1
    else:
        lcs.append(line_a[r])
        r, c = r-1, c-1

print(dp[-1][-1])
if lcs: print("".join(lcs[::-1]))