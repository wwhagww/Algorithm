x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def dir(vec, p):
    # vec 직선 기준 점 p의 위치 판별
    # 반시계 쪽에 있으면 +1 시계쪽에 있으면 -1 겹치면 0
    res = None
    if vec[0] == 0:
        if p[0] == 0: res = 0
        if p[0] > 0:
            if vec[1] > 0: res = -1
            if vec[1] < 0: res = 1
        if p[0] < 0:
            if vec[1] > 0: res = 1
            if vec[1] < 0: res = -1
        return res

    check_y = vec[1] * abs(p[0]) * (-1 if (vec[0]>0) ^ (p[0]>0) else 1)
    mod_y = p[1] * abs(vec[0])

    if mod_y == check_y: res = 0
    if mod_y > check_y:
        if vec[0] > 0: res = 1
        if vec[0] < 0: res = -1
    if mod_y < check_y:
        if vec[0] > 0: res = -1
        if vec[0] < 0: res = 1
    return res

def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    cross = True
    d1 = dir((x2-x1, y2-y1), (x3-x1, y3-y1))
    d2 = dir((x2-x1, y2-y1), (x4-x1, y4-y1))
    d3 = dir((x4-x3, y4-y3), (x1-x3, y1-y3))
    d4 = dir((x4-x3, y4-y3), (x2-x3, y2-y3))
    if d1 == d2:
        cross = False
    if d3 == d4:
        cross = False
    if d1 == d2 == d3 == d4 == 0:
        if x1 == x2:
            if max(y1,y2) < y3 and max(y1,y2) < y4 \
                or min(y1,y2) > y3 and min(y1,y2) > y4:
                cross = False
            else:
                cross = True
                
        else:
            if max(x1,x2) < x3 and max(x1,x2) < x4 \
                or min(x1,x2) > x3 and min(x1,x2) > x4:
                cross = False
            else:
                cross = True
                
    return cross

print(1 if is_cross(x1, y1, x2, y2, x3, y3, x4, y4) else 0)