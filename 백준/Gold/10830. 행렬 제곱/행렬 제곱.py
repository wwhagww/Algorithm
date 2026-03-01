N, B = map(int, input().split())
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

def matmul(a, b):
    c = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][j] += a[i][k]*b[k][j]
    for i in range(N):
        for j in range(N):
            c[i][j] %= 1000
    return c

def fast(mat, b):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        res[i][i] = 1
    
    while b:
        if b % 2 == 1:
            res = matmul(res, mat)
        b //= 2
        mat = matmul(mat, mat)
    return res

result = fast(mat, B)

for i in range(N):
    print(*result[i])