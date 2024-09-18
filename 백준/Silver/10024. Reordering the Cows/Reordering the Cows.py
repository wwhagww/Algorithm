n = int(input())

initial = []
for _ in range(n):
    initial.append(int(input()))
# print(initial)

correctIdx = {}
for i in range(n):
    correctIdx[int(input())] = i
# print(correctIdx)

cntCircuit = 0
maxLength = -1
isVisited = [False]*n
for i, v in enumerate(initial):
    if isVisited[i]: continue
    isVisited[i] = True
    if correctIdx[v] == i: continue
    cntCircuit += 1

    length = 1
    cur = v
    while correctIdx[cur] != i:
        isVisited[correctIdx[cur]] = True
        cur = initial[correctIdx[cur]]
        length += 1

    maxLength = max(maxLength, length)
# print(isVisited)
print(cntCircuit, maxLength)

