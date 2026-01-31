import sys; input=sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
is_san = True
state = 0
for i in range(1,N):
    prev = lst[i-1]
    cur = lst[i]
    if state == 0:
        if prev < cur:
            continue
        else:
            state = 1
    elif state == 1:
        if prev > cur:
            continue
        else:
            is_san = False
            break
print("YES" if is_san else "NO")