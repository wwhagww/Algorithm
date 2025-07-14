def calc_tri(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
          - (b[1] - a[1]) * (c[0] - a[0])) / 2
N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

res = 0
o = lst[0]
for i in range(1, N-1):
    res += calc_tri(o, lst[i], lst[i+1])
res = round(abs(res), 1)
print(res)