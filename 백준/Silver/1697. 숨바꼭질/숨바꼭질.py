import sys; input=sys.stdin.readline

ed, st = map(int, input().split())

def f(now, cnt = 0):
    if ed >= now or abs(ed-now)==1:
        cnt += abs(ed-now)
    else:
        if now % 2 == 0:
            if abs(ed-now) <= abs(ed-now//2):
                cnt += abs(ed-now)
            else:
                cnt = f(now//2, cnt+1)
        else:
            cnt = min(f(now-1, cnt+1), f(now+1, cnt+1))
    return(cnt)
print(f(st))