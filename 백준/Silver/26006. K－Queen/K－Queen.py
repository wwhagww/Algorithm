n, k = map(int, input().split())
kr, kc = map(int, input().split())
qRow = set()
qCol = set()
qDiaAdd = set()
qDiaSub = set()
for _ in range(k):
    r, c = map(int, input().split())
    qRow.add(r)
    qCol.add(c)
    qDiaAdd.add(r+c)
    qDiaSub.add(r-c)

def isAttacked(r, c):
    return (r in qRow or c in qCol or r+c in qDiaAdd or r-c in qDiaSub)

dr = [-1, -1, -1, 0, 0, 1, 1 ,1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
arounds = [(kr+dr[i], kc+dc[i]) for i in range(8) if (0 < kr+dr[i] <= n and 0 < kc+dc[i] <= n)]
isStale = True
for r, c in arounds:
    if isAttacked(r, c) == False: isStale = False
isCheck = isAttacked(kr, kc)

if isCheck:
    if isStale:
        print("CHECKMATE")
    else: print("CHECK")
elif isStale:
    print("STALEMATE")
else: print("NONE")