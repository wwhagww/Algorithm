from collections import Counter
N = int(input())
A, B, C, D = zip(*[map(int, input().split()) for _ in range(N)])
AB = Counter(a + b for a in A for b in B)
res = 0
for c in C:
    for d in D:
        res += AB.get(-(c+d), 0)
print(res)