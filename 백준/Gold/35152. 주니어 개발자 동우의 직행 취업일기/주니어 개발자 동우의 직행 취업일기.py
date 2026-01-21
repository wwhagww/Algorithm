N = int(input())
if N <= 10**6 - 3:
    print(N+3)
    print(N+3,N+2)
    print(N+2,N+1)
    for i in range(1, N+1):
        print(N+1, i)
elif N % 2 == 0:
    print(4+N//2)
    print(N//2 + 4, N//2 + 2)
    print(N//2 + 3, N//2 + 2)
    print(N//2 + 1, N//2 + 2)
    for i in range(1, N//2+1):
        print(N//2 + 1, i)
else:
    print(5+N//3)
    print(N//3 + 5, N//3 + 2)
    print(N//3 + 4, N//3 + 2)
    print(N//3 + 3, N//3 + 2)
    print(N//3 + 1, N//3 + 2)
    for i in range(1, N//3+1):
        print(N//3 + 1, i)

