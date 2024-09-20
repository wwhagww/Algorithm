import math
n = int(input())
lst = list(map(int, input().split()))
t, p = map(int, input().split())
cntTs = 0
cntPs, cntP = 0, 0
for cnt in lst:
    cntTs += math.ceil(cnt/t)
cntPs = n // p
cntP = n % p
print(cntTs)
print(cntPs, cntP)