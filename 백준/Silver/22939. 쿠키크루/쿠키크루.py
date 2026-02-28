from itertools import permutations
# 침투단(Assassin) - 젤리(J)
# 치유단(Healer) - 초콜릿(C)
# 마법단(Mage) - 베리(B)
# 방어단(Tanker) - 호두(W)

N = int(input())
lst = [[] for _ in range(4)]
for i in range(N):
    line = list(input())
    for j, c in enumerate(line):
        if c == "H":
            HOME = (i,j)
        elif c == "#":
            END = (i,j)
        elif c == "J":
            lst[0].append((i,j))
        elif c == "C":
            lst[1].append((i,j))
        elif c == "B":
            lst[2].append((i,j))
        elif c == "W":
            lst[3].append((i,j))

def eval(arr):
    res = 0
    pi, pj = arr[0]
    for (i, j) in arr[1:]:
        res += abs(pi-i) + abs(pj-j)
        pi, pj = i, j
    # print(arr, res)
    return res

# print(lst)
# print(list(permutations(lst[0],3)))
trim = [min(map(lambda x: eval((HOME,)+x+(END,)), list(permutations(lst[i])) )) for i in range(4)]
# print(trim)
min_idx = 0
min_val = trim[0]
for i in range(1, 4):
    if trim[i] < min_val:
        min_idx = i
        min_val = trim[i]
dct = [
    "Assassin",
    "Healer",
    "Mage",
    "Tanker"
]
print(dct[min_idx])