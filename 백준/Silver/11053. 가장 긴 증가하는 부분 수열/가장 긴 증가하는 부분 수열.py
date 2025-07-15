import sys; read=sys.stdin.readline
N = int(read())
inp = list(map(int, read().split()))
lst = []
for num in inp:
    cnt = 1
    for idx, i in enumerate(lst):
        if inp[idx] < num and i >= cnt:
            cnt = i+1
    lst.append(cnt)
print(max(lst))
    