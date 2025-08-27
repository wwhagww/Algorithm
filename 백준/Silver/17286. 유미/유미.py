def dist(a, b):
    return (abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2)**0.5

o = tuple(map(int, input().split()))
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))

print(int(min(
    dist(o, a)+dist(a,b)+dist(b,c),
    dist(o, a)+dist(a,c)+dist(c,b),
    dist(o, b)+dist(b,a)+dist(a,c),
    dist(o, b)+dist(b,c)+dist(c,a),
    dist(o, c)+dist(c,b)+dist(b,a),
    dist(o, c)+dist(c,a)+dist(a,b),
)))
