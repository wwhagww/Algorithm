# 볼록 껍질
import sys; input=sys.stdin.readline
N = int(input())
inp = []
INF = float("inf")
r = (INF, INF)
for i in range(N):
    p = tuple(map(int, input().split()))
    inp.append(p)
    if p[0] < r[0] or (p[0] == r[0] and p[1] < r[1]):
        r = p
# 시작점은 제일 왼쪽, x 좌표 같은거 여러개면 그 중 제일 아래

def ccw(a, b, c): # ccw > 0 일때 반시계
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

# 기울기 오름차순 정렬 
arr = sorted(
    [p for p in inp if p != r], 
    key=lambda p:(
        ((p[1]-r[1]) / (p[0]-r[0])) if p[0]-r[0] != 0 else float("inf"),
        dist(r, p)
        )
    )

# 기울기 작은것부터 순회 = 아래부터 감싸기
stk = [r, arr[0]]
for p in arr[1:]:
    while True:
        if stk[-1] == r: 
            stk.append(p)
            continue
        check = ccw(stk[-2], stk[-1], p)
        if check < 0: # 시계방향
            stk.pop()
            continue
        elif check == 0: # 한 직선 위
            if dist(stk[-2], p) > dist(stk[-2], stk[-1]):
                stk.pop()
                stk.append(p)
            break
        else: # 반시계방향
            stk.append(p)
            break

print(len(stk))
