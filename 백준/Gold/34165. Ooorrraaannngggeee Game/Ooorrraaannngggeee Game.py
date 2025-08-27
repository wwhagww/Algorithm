s = input()
target = "orange"
target_map = {c: i for i, c in enumerate(target)}
dp = [[0] * 6 for _ in range(6)]
for char in s:
    if char not in target_map:
        continue
    idx = target_map[char]
    if idx == 0:
        dp[0][0] += 1
        continue

    len1 = 0
    if sum(dp[idx]) > 0:
        len1 = sum(dp[idx]) + 1
    len2 = 0
    if sum(dp[idx-1]) > 0:
        len2 = sum(dp[idx-1]) + 1

    if len1 > len2:
        dp[idx][idx] += 1
    elif len2 > len1:
        dp[idx] = dp[idx-1][:]
        dp[idx][idx] = 1
    elif len1 > 0:
        dp[idx] = dp[idx-1][:]
        dp[idx][idx] = 1

cnts = dp[5]
lenf = sum(cnts)

if lenf == 0:
    print(0)
else:
    print(lenf)
    res = ""
    for i in range(6):
        res += target[i] * cnts[i]
    print(res)