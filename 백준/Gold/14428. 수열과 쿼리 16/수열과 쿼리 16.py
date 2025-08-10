import sys; input=sys.stdin.readline
N = int(input())
size = 1
while size < N: size *= 2
arr = list(map(int, input().split()))

def f(a, b):
    if a is None: return b
    if b is None: return a
    ia, va = a
    ib, vb = b
    if va < vb:
        return a
    elif va == vb:
        return (min(ia,ib), va)
    else:
        return b

tree = [None]*(size*2)
for i in range(N):
    tree[size+i] = (i, arr[i])
for i in reversed(range(1,size)):
    tree[i] = f(tree[2*i], tree[2*i+1])

# print(tree)

M = int(input())
for _ in range(M):
    command, a, b = map(int, input().split())

    if command == 1: # 갱신
        i, v = a-1, b
        tree[size+i] = (i, b)
        idx = (size+i) // 2
        while idx:
            tree[idx] = f(tree[2*idx], tree[2*idx+1])
            idx //= 2

    if command == 2: # 쿼리
        l, r = a-1 + size, b-1 + size
        res = None
        while l <= r:
            if l % 2 == 1:
                res = f(res, tree[l])
                l += 1
            if r % 2 == 0:
                res = f(res, tree[r])
                r -= 1
            l //= 2
            r //= 2
        print(res[0]+1)