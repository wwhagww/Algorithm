n = int(input())
lst = [0]*n
for _ in range(n-1):
    x, y = map(int, input().split())
    lst[x-1] += 1
    lst[y-1] += 1
print(max(lst)+1)