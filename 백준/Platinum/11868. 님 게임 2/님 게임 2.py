N = int(input())
arr = list(map(int, input().split()))
res = 0
for num in arr:
    res ^= num

if res == 0:
    print("cubelover")
else:
    print("koosaga")