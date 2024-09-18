while True:
    try: n = int(input())
    except: break
    board = []
    rows = [0]*n
    cols = [0]*n
    for r in range(n):
        line = list(input())
        board.append(line)
        for c, v in enumerate(line):
            rows[r] += ord(v)
            cols[c] += ord(v)
    correctValue = rows[0] if (rows[0]==rows[1] or rows[0]==rows[2]) else rows[1]
    # print(rows, cols, correctValue)
    row = [r for r, v in enumerate(rows) if v != correctValue][0]
    col = [c for c, v in enumerate(cols) if v != correctValue][0]
    print(row+1, col+1, chr(correctValue-rows[row]+ord(board[row][col])))