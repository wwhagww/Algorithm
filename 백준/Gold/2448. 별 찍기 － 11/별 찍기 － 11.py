G = int(input())
res = ["" for _ in range(G)]
res[0] = "  *  "
res[1] = " * * "
res[2] = "*****"

n = 3
while n < G:
    for i in range(n, 2*n):
        res[i] = res[i-n] + " " + res[i-n]
    for i in range(n):
        res[i] = " "*n + res[i] + " "*n
    n *= 2

print(*res, sep="\n")