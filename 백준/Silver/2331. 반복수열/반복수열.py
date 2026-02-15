A, P = map(int, input().split())
visited = [False]*1000000
arr = [A]
visited[A] = True
while True:
    tmp = list(map(int, str(arr[-1])))
    # print(tmp)
    res = 0
    for num in tmp:
        res += num**P

    arr.append(res)
    if visited[res]: 
        break
    visited[res] = True
print(arr.index(arr[-1]))
