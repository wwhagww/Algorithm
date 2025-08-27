dp = ["\n", "#\n"]
for i in range(2, 11):
    res = (
        "#"*i + "\n" + 
        ("#" + "J"*(i-2) + "#\n") * (i-2 if i > 2 else 0) +
        "#"*i + "\n"
        )
    dp.append(res)
T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])