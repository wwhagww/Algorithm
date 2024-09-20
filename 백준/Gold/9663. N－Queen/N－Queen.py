n = int(input())
cols = [False]*n
diaSubs = [False]*(2*n-1) # \
diaAdds = [False]*(2*n-1) # /

# 줄별로 1개씩 DFS랑 비슷하게

def dfs(row, n):
    cntCase = 0
    for col in range(n):
        diaSub = row - col + (n-1) # 0 ~ 2n-2
        diaAdd = row + col # 0 ~ 2n-2
        # print(row, col)
        if cols[col] or diaAdds[diaAdd] or diaSubs[diaSub]:
            continue

        cols[col], diaAdds[diaAdd], diaSubs[diaSub] = True, True, True

        if row < n-1: cntCase += dfs(row+1, n)
        else: cntCase += 1
        
        cols[col], diaAdds[diaAdd], diaSubs[diaSub] = False, False, False
    return cntCase

print(dfs(0, n))