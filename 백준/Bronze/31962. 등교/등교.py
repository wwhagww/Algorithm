N, X = map(int, input().split())
lst = []
for _ in range(N):
    s, t = map(int, input().split())
    if s+t <= X: lst.append(s)
if len(lst)==0:
    print(-1)
else:
    lst.sort(reverse=True)
    print(lst[0])