# LCS (최장 공통 부분 수열)
word1 = input()
word2 = input()
len1 = len(word1)
len2 = len(word2)
dp = [[0]*(len2+1) for _ in range(len1+1)]
for x in range(1, len1+1):
    for y in range(1, len2+1):
        if word1[x-1] == word2[y-1]:
            dp[x][y] = dp[x-1][y-1] + 1
        else:
            dp[x][y] = max(dp[x-1][y], dp[x][y-1])
# print("\n".join(str(dp)[2:-2].split("], [")))
print(dp[-1][-1])