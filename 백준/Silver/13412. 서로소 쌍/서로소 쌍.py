T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1: 
        print(1)
        continue
    cnt = 0
    step = 2
    while N > 1:
        # print(N, step)
        if N % step != 0:
            step+=1
            continue
        cnt += 1
        while N % step == 0:
            N //= step
        step += 1
    print(2**(cnt-1))