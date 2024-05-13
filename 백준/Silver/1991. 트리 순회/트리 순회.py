# 트리 순회
N = int(input())
ci = {".":None}
ic = {}
for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    ci[c] = i
    ic[i] = c
data = [[None, None] for _ in range(N)]
for i in range(N):
    p, l, r = input().split()
    data[ci[p]][0] = ci[l]
    data[ci[p]][1] = ci[r]

def pre_ord(x):
    if x == None: return ""
    res = ic[x] + pre_ord(data[x][0]) + pre_ord(data[x][1])
    return res

def in_ord(x):
    if x == None: return ""
    res = in_ord(data[x][0]) + ic[x] + in_ord(data[x][1])
    return res

def post_ord(x):
    if x == None: return ""
    res = post_ord(data[x][0]) + post_ord(data[x][1]) + ic[x]
    return res

print(pre_ord(0))
print(in_ord(0))
print(post_ord(0))