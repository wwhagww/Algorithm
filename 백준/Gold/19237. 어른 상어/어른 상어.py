# 어른 상어 19237
N, M, k = map(int, input().split())
brd = []
int_1 = lambda x: int(x)-1
for _ in range(N):
    brd.append(list(map(int_1, input().split())))
dir = list(map(int_1, input().split()))
prr = [[] for _ in range(M)]
for i in range(M):
    for _ in range(4):
        prr[i].append(list(map(int_1, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

brd_s = [[-1]*N for _ in range(N)]
brd_t = [[0]*N for _ in range(N)]
cnt = 0
def spoil():
    global N
    for x in range(N):
        for y in range(N):
            if brd[x][y] == -1: continue
            brd_s[x][y] = brd[x][y]
            brd_t[x][y] = k

def move_all():
    global N, cnt
    brd_n = [[-1]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if brd[x][y] == -1: continue
            s = brd[x][y]
            cand = [(nx, ny, d) for d in [prr[s][dir[s]][i] for i in range(4)] if 0<=(nx:=x+dx[d])<N and 0<=(ny:=y+dy[d])<N]
            cand_1 = [(nx, ny, d) for nx, ny, d in cand if brd_t[nx][ny] == 0]
            cand_2 = [(nx, ny, d) for nx, ny, d in cand if brd_s[nx][ny] == s]
            cand = cand_1 + cand_2 + cand
            nx, ny, d = cand[0]
            if brd_n[nx][ny] != -1:
                cnt += 1
                brd_n[nx][ny] = min(brd_n[nx][ny], s)
            else:
                brd_n[nx][ny] = s
            dir[s] = d
    return brd_n
                
def dec():
    global N
    for x in range(N):
        for y in range(N):
            if brd_s[x][y] == -1: continue
            brd_t[x][y] -= 1
            if brd_t[x][y] == 0:
                brd_s[x][y] = -1
                
for time in range(1, 1001):
    spoil() # brd_t, s 갱신
    # print("\n".join(str(brd)[2:-2].split("], ["))) #
    brd = move_all() # brd, cnt, dir 갱신
    dec() # # brd_t, s 갱신
    
    if cnt == M-1:
        print(time)
        break
else:
    print(-1)