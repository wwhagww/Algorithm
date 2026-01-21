import sys; input = sys.stdin.readline
dct = {
    "X":[1,-3,2],
    "Y":[3,2,-1],
    "Z":[-2,1,3],
    "XX":[1,-2,-3],
    "YY":[-1,2,-3],
    "ZZ":[-1,-2,3],
    "XY":[1,2,-3],
    "YX":[1,2,-3],
    "YZ":[-1,2,3],
    "ZY":[-1,2,3],
    "ZX":[1,-2,3],
    "XZ":[1,-2,3]
}

state = [(1,2,3),]
N = int(input())
oprs = input().split()

for o in oprs:
    opr = dct[o]
    cur = [0]*3
    for idx, tar in enumerate(opr):
        tidx = abs(tar)-1
        sign = tar//abs(tar)
        cur[idx] = sign * state[-1][tidx]
    state.append(cur)

Q = int(input())
for _ in range(Q):
    L,R = map(int,input().split())
    prev = state[L-1]
    cur = state[R]
    for p in prev:
        res = []
        for c in cur:
            if abs(p)==abs(c):
                res.append(1 if p==c else -1)
            else:
                res.append(0)
        print(*res)
    

