def simulate(dir, board):
    new_board = [[] for _ in range(N)]
    # print(dir)
    if dir==1:
        board = [line[::-1] for line in board]
    elif dir==2:
        board = list(map(list, zip(*board)))
    elif dir==3:
        board = list(map(list, zip(*board)))
        board = [line[::-1] for line in board]
    for i in range(N):
        prev = None
        for j in range(N):
            if board[i][j] == 0: continue
            if prev:
                if prev == board[i][j]:
                    new_board[i].append(prev*2)
                    prev = None
                else:
                    new_board[i].append(prev)
                    prev = board[i][j]
            else:
                prev = board[i][j]
        else:
            if prev: new_board[i].append(prev)
            new_board[i] = new_board[i] + [0]*(N - len(new_board[i]))
    if dir==1:
        new_board = [line[::-1] for line in new_board]
    elif dir==2:
        new_board = list(map(list, zip(*new_board)))
    elif dir==3:
        new_board = [line[::-1] for line in new_board]
        new_board = list(map(list, zip(*new_board)))
    # print(new_board)
    return new_board

def dfs(move, board):
    if move == 0:
        return max(map(max, board))
    mx = max(map(max, board))
    for i in range(4):
        new_board = simulate(i, board)
        if new_board != board: 
            mx = max(mx, dfs(move-1, new_board))
    return mx

N = int(input())
board = [list(map(int , input().split())) for _ in range(N)]
print(dfs(5, board))