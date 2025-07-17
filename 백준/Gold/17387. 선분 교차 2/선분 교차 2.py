def ccw(x1, y1, x2, y2, x3, y3):
    val = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
    if val > 0: return 1
    if val < 0: return -1
    return 0

def is_cross(x1,y1,x2,y2, x3,y3,x4,y4):
    d1 = ccw(x1,y1,x2,y2,x3,y3)
    d2 = ccw(x1,y1,x2,y2,x4,y4)
    d3 = ccw(x3,y3,x4,y4,x1,y1)
    d4 = ccw(x3,y3,x4,y4,x2,y2)

    if d1 * d2 <= 0 and d3 * d4 <= 0:
        if d1 == d2 == d3 == d4 == 0:
            def in_range(a, b, c):
                return min(a,b) <= c <= max(a,b)
            return (
                in_range(x1,x2,x3) or in_range(x1,x2,x4) or
                in_range(x3,x4,x1) or in_range(x3,x4,x2)
            ) and (
                in_range(y1,y2,y3) or in_range(y1,y2,y4) or
                in_range(y3,y4,y1) or in_range(y3,y4,y2)
            )
        return True
    return False

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
print(1 if is_cross(x1,y1,x2,y2,x3,y3,x4,y4) else 0)