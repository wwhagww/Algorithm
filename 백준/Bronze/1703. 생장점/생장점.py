while True:
    inp = list(map(int, input().split()))
    if inp[0] == 0: break
    year = inp[0]
    split = inp[1::2]
    cut = inp[2::2]
    res = 1
    for i in range(year):
        res *= split[i]
        res -= cut[i]
    print(res)