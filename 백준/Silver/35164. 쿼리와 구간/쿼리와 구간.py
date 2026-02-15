N, M = map(int,input().split())
arr = []
for _ in range(M):
    arr.append(int(input()))
if N == 2:
    if 0 not in arr:
        print(1)
        print(1,0,2)
        print(1,0,2)
        for _ in range(M):
            print(2,1,2)
    elif 1 not in arr:
        print(1)
        print(1,0,2)
        print(1,4,5)
        for _ in range(M):
            print(2,1,2)
    else:
        print(-1)
else:
    print(1)
    print(1,0,2)
    print(1,0,2)
    print(1,4,6)
    for _ in range(N-3):
        print(1,0,2)
    for num in arr:
        if num == 1:
            print(2,1,2)
        else:
            print(2,1,3)