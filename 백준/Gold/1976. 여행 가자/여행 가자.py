# 여행 계획 > 여행 가자

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
        
def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
        
N = int(input())
M = int(input())

parent = [i for i in range(N)]

for i in range(N):
    for j, tf in enumerate(map(int, input().split())):
        if tf == 1:
            union(parent, i, j)
plan = list(map(lambda x:int(x)-1, input().split()))
if all([parent[i] == parent[plan[0]] for i in plan]):
    print("YES")
else:
    print("NO")