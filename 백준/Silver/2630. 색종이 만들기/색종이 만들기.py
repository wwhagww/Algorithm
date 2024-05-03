N = int(input())
data = []
for _ in range(N):
    data.append(input().split())
def check(ls, le, cs, ce): # 전부 같으면 0 1 다르면 False
    for l in range(ls, le):
        for c in range(cs, ce):
            if data[l][c] != data[ls][cs]:
                return False
    return True
cnt = {"0":0, "1":0}
def f(ls, le, cs, ce):
    if check(ls, le, cs, ce): 
        cnt[data[ls][cs]] += 1
        return
    f(ls, (ls+le)//2, cs, (cs+ce)//2)
    f(ls, (ls+le)//2, (cs+ce)//2, ce)
    f((ls+le)//2, le, cs, (cs+ce)//2)
    f((ls+le)//2, le, (cs+ce)//2, ce)
f(0, N, 0, N)
print(cnt["0"])
print(cnt["1"])