n, m = map(int, input().split())
for _ in range(m):
    lst = list(map(int, input().split()))
    cnt = dict([(n, lst.count(n)) for n in range(-2, 3)])
    ans = 2**cnt[2]
    ans *= 4**(cnt[-2]//2)
    if cnt[-1]>0 and cnt[-2]%2==1:
        ans *= 2
    if ans == 1 and cnt[1]==0 and cnt[-1]//2==0: 
        ans = max(lst)
        
    print(ans)