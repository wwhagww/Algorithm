lst = [str(i).count("0") for i in range(1000001)]
# print(lst)
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(sum(lst[n:m+1]))