score = tuple(map(int, input().split()))
N = int(input())
mx = 0
for _ in range(N):
    sm = 0
    for _ in range(3):
        sm += sum([score[i]*c for i, c in enumerate(map(int, input().split()))])
    mx = max(mx, sm)
print(mx)