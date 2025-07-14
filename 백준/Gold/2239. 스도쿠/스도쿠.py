board = [list(map(int, input())) for _ in range(9)]

def dfs(n):
    if n==81: return True
    i, j = n // 9, n % 9
    # 채워져있는 칸이면 다음칸 dfs 호출. 결과값 그대로 반환
    if board[i][j] != 0: return dfs(n+1)
    # print(i, j) ###
    # 후보 선택
    cand = sorted(list(set(range(1, 10)) 
    - set(board[i]) 
    - set([board[ii][j] for ii in range(9)])
    - set([board[(i//3)*3 + t//3][(j//3)*3 + t%3] for t in range(9)])
    ))
    # print(cand) ###
    # 가능한 후보 없으면 False 반환
    if len(cand) == 0: return False
    for c in cand:
        board[i][j] = c
        # print(c) ###
        # 좌표 다음 칸으로 해서 dfs 호출
        if dfs(n+1): return True
        # 완성하면 True 실패하면 False 반환
        # True면 True 바로 반환
        # 실패했으면 다음 후보
    else:
        # 모든 후보 실패했으면 칸 되돌리고 False 반환
        board[i][j] = 0
        return False

dfs(0)
for line in board:
    print("".join(map(str, line)))