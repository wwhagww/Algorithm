n = int(input())
for _ in range(n):
    y, m, d = map(int, input().split())
    x = y * 400 + m * 40 + d
    if x <= 1989 * 400 + 2 * 40 + 27:
        print("Yes")
    else: print("No")