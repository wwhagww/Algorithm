import sys; input=sys.stdin.readline
N = int(input())

stack = [(int(input()), 1)]
cnt = 0
for _ in range(N-1):
    cur = int(input())
    tmp = 0
    prev = None
    while stack:
        if stack[-1][0] <= cur:
            prev, prev_cnt = stack.pop()
            tmp += prev_cnt
        else:
            tmp += 1
            break
    cnt += tmp
    stack.append((cur, prev_cnt+1 if prev == cur else 1))
print(cnt)