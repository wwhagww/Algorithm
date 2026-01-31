import sys; input=sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
H, L = max(lst[0],lst[-1]), min(lst[0],lst[-1])
if (N-2) < H-L:
    print(H-(N-2))
else:
    print((H+L-(N-2)+1)//2)