from collections import Counter
N, M = map(int, input().split())
cnt = Counter()
for _ in range(N):
    cnt += Counter(input())

wall = cnt["#"] 
v1 = sum([cnt["U"],cnt["D"],cnt["R"],cnt["L"]])
va = cnt["A"]
vc = cnt["V"]
s = cnt["S"]
e = cnt["E"]
if s == 1 and e == 1:
        
    if wall <= 1 and v1 <= 1 and va == 0 and vc == 0:
        print(1)
    elif va == 0 and vc == 0:
        print(2)
    elif va == 0:
        print(3)
    else:
        print(4)
else:
    print(-1)