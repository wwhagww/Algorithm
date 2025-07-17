from collections import deque, defaultdict
T = int(input())
WALL = "*"
ROAD = "."
for _ in range(T):
    H, W = map(int, input().split())
    board = []
    for _ in range(H):
        board.append(list(input()))
    passable = set(key.upper() for key in input() if key.islower())

    visited = [[False]*W for _ in range(H)]
    deq = deque(
        [(0, c) for c in range(W) if board[0][c] != WALL]
        + [(H-1, c) for c in range(W) if board[H-1][c] != WALL]
        +[(r, 0) for r in range(1, H-1) if board[r][0] != WALL]
        +[(r, W-1) for r in range(1, H-1) if board[r][W-1] != WALL]
        )

    cnt = 0
    skipped = defaultdict(list)
    while deq:
        r, c = deq.popleft()
        if visited[r][c]: continue
        sq = board[r][c]

        if sq.isupper() and sq not in passable:
            skipped[sq].append((r, c))
            continue

        visited[r][c] = True

        if sq.islower():
            sq = sq.upper()
            if sq not in passable:
                passable.add(sq)
                deq.extend(skipped[sq])

        if sq == "$":
            cnt += 1

        for nr, nc in [(r-1, c),(r+1, c), (r, c-1), (r, c+1)]:
            if nr < 0 or nr >= H or nc < 0 or nc >= W: continue
            if board[nr][nc] == WALL or visited[nr][nc]: continue
            deq.append((nr, nc))

    print(cnt)
