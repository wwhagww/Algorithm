import sys; read = sys.stdin.readline

class SegTree():
    def __init__(self, arr:list, f, ini=0):
        n = len(arr)
        size = 1
        while size < n: size *= 2
        tree = [ini] * (2 * size)
        for i in range(n):
            tree[size + i] = arr[i]
        for i in range(size-1, 0, -1):
            tree[i] = f(tree[2*i], tree[2*i + 1])
        
        self.size = size
        self.tree = tree
        self.f = f
        self.ini = ini

    def range_query(self, l, r):
        l += self.size
        r += self.size
        res = self.ini
        while l <= r:
            if l % 2 == 1:
                res = self.f(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = self.f(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(read()))

max_tree = SegTree(arr, max, 0)
min_tree = SegTree(arr, min, 1e9+1)
for _ in range(M):
    a, b = map(int, read().split())
    (a, b) = (a-1, b-1) if a < b else (b-1, a-1)
    print(min_tree.range_query(a, b), max_tree.range_query(a, b))