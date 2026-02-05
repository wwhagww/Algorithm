from collections import Counter
T = int(input())
for _ in range(T):
    line = list(map(int,input().split()))
    N = line[0]
    cnts = Counter(line[1:])
    for i, v in cnts.items():
        if v > N//2:
            print(i)
            break
    else: 
        print("SYJKGW")