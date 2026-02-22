N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
na = []
nb = []
ta = []
tb = []
A.sort()
B.sort()
cnt = 0
i,j = 0,0
while i < N and j < N:
    if A[i] == B[j]:
        na.append(A[i])
        nb.append(B[j])
        cnt += 1
        i+=1;j+=1
    elif A[i] > B[j]:
        tb.append(B[j])
        j += 1
    else:
        ta.append(A[i])
        i += 1
else:
    na.extend(ta)
    nb.extend(tb)
    if i < N:
        na.extend(A[i:N])
    if j < N:
        nb.extend(B[j:N])
print(cnt)
print(*na)
print(*nb)