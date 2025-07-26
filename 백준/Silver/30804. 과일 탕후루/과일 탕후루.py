N = int(input())
lst = input().split()

mem = [None, None]
left = [0,0]
right = [0,0]

mx = 0
for idx in range(N):
    cur = lst[idx]
    if cur == mem[0]:
        right[0] = idx
    elif cur == mem[1]:
        right[1] = idx

    elif mem[0] is None:
        mem[0],left[0],right[0] = cur, idx, idx
    elif mem[1] is None:
        mem[1],left[1],right[1] = cur, idx, idx

    else:
        out = 0 if right[0] < right[1] else 1
        mx = max(mx, idx - min(left))

        left[1 if out==0 else 0] = right[out]+1
        mem[out], left[out], right[out] = cur, idx, idx
    # print(mem, left, right, mx)

else:
    mx = max(mx, N - min(left))
    # print(mem, left, right, mx)

print(mx)