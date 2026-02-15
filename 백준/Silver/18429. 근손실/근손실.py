from itertools import permutations
N, K = map(int, input().split())

arr = list(map(int,input().split()))
for i in range(N):
    arr[i] -= K
arr.sort()

per = permutations(arr, N)
res = 0
for tmp in per:
    sm = 0
    for num in tmp:
        sm += num
        if sm < 0:
            break
    else:
        res += 1
print(res)