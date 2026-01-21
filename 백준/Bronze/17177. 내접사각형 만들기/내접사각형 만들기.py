from math import sqrt
lst = list(map(int, input().split()))
lst.sort()
tmp = (int(sqrt((lst[2]**2-lst[0]**2)*(lst[2]**2-lst[1]**2)))-lst[0]*lst[1])//lst[2]
if tmp <= 0:
    print(-1)
else:
    print(tmp)