import sys; read=sys.stdin.readline

def mul(a, b):
    return a*b%1000000007

class SegTree():
    def __init__(self, arr:list, f, ini=0):
        n = len(arr)
        size = 1
        while size < n: size *= 2
        tree = [ini] * (2 * size)
        for i in range(n):
            tree[size + i] = arr[i]
        for i in reversed(range(1, size)):
            tree[i] = f(tree[2*i], tree[2*i + 1])
        
        self.size = size
        self.tree = tree
        self.f = f
        self.ini = ini

    def __setitem__(self, idx, val):
        idx += self.size
        self.tree[idx] = val
        idx //= 2
        while idx>0:
            self.tree[idx] = self.f(self.tree[2*idx], self.tree[2*idx + 1])
            idx //= 2

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
    


N, M, K = map(int, read().split())
arr = []
for _ in range(N):
    arr.append(int(read()))

tree = SegTree(arr, mul, 1)
for _ in range(M+K):
    a, b, c = map(int, read().split())
    if a==1:
        tree[b-1] = c
    else:
        print(tree.range_query(b-1, c-1))