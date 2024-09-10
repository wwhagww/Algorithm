def median(lst):
    return sorted(lst)[len(lst)//2]

m, n, k, w = map(int, input().split())
# m행 n열
board = []
for _ in range(m):
    board.append(list(map(int, input().split())))
# print(board)
newBoard = [[0]*(n-w+1) for _ in range(m-w+1)]
for i in range(m-w+1):
    for j in range(n-w+1):
        cand = []
        for newLine in [line[j:j+w] for line in board[i:i+w]]:
            cand.extend(newLine)
        newBoard[i][j] = median(cand)

for line in newBoard:
    print(" ".join(map(str, line)))