import sys; read = sys.stdin.readline
from collections import defaultdict
n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, read().split())
    lst.append((a, b) if a < b else (b, a))
d = int(input())

dct = defaultdict(int)
for a, b in lst:
    if (b - d) <= a:
        dct[b-d] += 1
        dct[a+1] -= 1

mx_cnt = 0
cnt = 0
for _, dcnt in sorted(list(dct.items())):
    cnt += dcnt
    mx_cnt = max(mx_cnt, cnt)
print(mx_cnt)