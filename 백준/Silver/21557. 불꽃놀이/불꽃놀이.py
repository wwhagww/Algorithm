import sys; input=sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
H, L = max(lst[0],lst[-1]), min(lst[0],lst[-1])
if L-1 <= H-(N-2):
    print(H-(N-2))
else:
    print((H+L-(N-2))//2)