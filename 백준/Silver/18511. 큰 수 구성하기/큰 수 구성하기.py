n, k = input().split()
nList = list(map(int, n))

cand = list(map(int, input().split()))
cand.sort()

answer = []
lastNotMin = -1
for idx, num in enumerate(nList):
    if num in cand: 
        answer.append(num)
        if num != cand[0]: lastNotMin = idx
    else:
        if cand[0] < num:
            for c in cand:
                if c < num: tmp = c
            answer.append(tmp)
            answer.extend([cand[-1]] * (len(nList)-len(answer)))
        else:
            if lastNotMin == -1:
                answer = [cand[-1]] * (len(nList)-1)
            else:
                answer = answer[:lastNotMin]
                for c in cand:
                    if c < nList[lastNotMin]: tmp = c
                answer.append(tmp)
                answer.extend([cand[-1]] * (len(nList)-len(answer)))
        break
print("".join(map(str, answer)))