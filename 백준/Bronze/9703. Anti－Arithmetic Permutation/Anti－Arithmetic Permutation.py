# n은 3~50
# 0 ~ n-1까지의 리스트에 인덱스를 담아
# 처음부터 1칸, 2칸, ... 단위로 순회하면서 인덱스가 3연속 늘거나 주는 경우가 있는지 확인
# 7개면 0 3 6, 3차이까지. 6개면 2차이까지만 확인. (n-1) // 2

def isArith(lst):
    prev = lst[0] < lst[1]
    for i in range(1, len(lst)-1):
        now = lst[i] < lst[i+1]
        if prev == now: return True
        else: prev = now
    else: return False

t = int(input())
for ti in range(t):
    n = int(input())
    inp = list(map(int, input().split()))

    idxs = [0]*n
    for i, v in enumerate(inp):
        idxs[v] = i
    # print("#", idxs)

    answer = "YES"
    for term in range(1,(n-1)//2 + 1):
        for i in range(term):
            if isArith(idxs[i::term]):
                answer = "NO"
                break
        else: continue
        break
    print(f"Case #{ti+1}: {answer}")