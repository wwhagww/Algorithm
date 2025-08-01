import sys; read = sys.stdin.readline

N, M, K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(int(read()))

def build_tree(arr):
    n = len(arr)
    size = 1
    while size < n:
        size *= 2
    tree = [0] * (2 * size)
    # leaf 채우기
    for i in range(n):
        tree[size + i] = arr[i]
    # 부모 노드 만들기
    for i in range(size - 1, 0, -1): # size-1 ~> 1
        tree[i] = tree[2 * i] + tree[2 * i + 1]
    return tree, size

def update_tree(tree, size, i, num):
    i += size
    diff = num - tree[i]
    while i:
        tree[i] += diff
        i //= 2

def range_sum(tree, size, l, r):
    # leaf 인덱스로 이동
    l += size  
    r += size
    res = 0
    while l <= r:
        if l % 2 == 1:  # l이 오른쪽 자식이면 독립 노드로 사용
            res += tree[l]
            l += 1
        if r % 2 == 0:  # r이 왼쪽 자식이면 독립 노드로 사용
            res += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return res

tree, size = build_tree(arr)

for _ in range(M+K):
    a, b, c = map(int, read().split())
    if a==1:
        update_tree(tree, size, b-1, c)
        # print(tree)
    else: # a==2
        res = range_sum(tree, size, b-1, c-1)
        print(res)