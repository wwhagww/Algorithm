T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    roads = []
    for _ in range(M):
        s, e, t = map(int, input().split())
        s-=1; e-=1
        roads.append((s, e, t))
        roads.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        s-=1; e-=1
        roads.append((s, e, -t))

    dist = [0]*N

    for _ in range(N-1):
        for s,e,t in roads:
            dist[e] = min(dist[e], dist[s]+t)

    for s, e, t in roads:
        if dist[s]+t < dist[e]:
            print("YES")
            break
    else:
        print("NO")
