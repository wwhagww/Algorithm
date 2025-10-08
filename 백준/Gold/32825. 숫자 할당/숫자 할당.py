A,B,C,D,E,F,G,H = map(int, input().split())
cnt = 0
check = [False]*14
for d in range(1, 14 if 14<D else D):
    h = D-d
    if h > 13 or h == d: continue
    check[d], check[h] = True, True
    E, F = E-d, F-h
    
    for l in range(1, min(14,H)):
        m = H-l
        if m > 13 or m == l: continue
        if check[l] or check[m]: continue
        check[l], check[m] = True, True
        A, B = A-l, B-m
        if min(A,B,C,E,F,G) >= 6:
            for k in range(1, min(14,C,G)):
                if check[k]: continue
                check[k] = True
                C, G = C-k, G-k

                for c in range(1, min(14,C)):
                    g = C-c
                    if g > 13 or g == c: continue
                    if check[c] or check[g]: continue
                    check[c], check[g] = True, True
                    E, F = E-c, F-g

                    for i in range(1, min(14,G)):
                        j = G-i
                        if j > 13 or i == j: continue
                        if check[i] or check[j]: continue
                        check[i], check[j] = True, True
                        A, B = A-i, B-j

                        if min(A,B,E,F) >= 3:
                            for a in range(1, min(14, A, E)):
                                b, e = E-a, A-a
                                if b > 13 or e > 13 or a==b or a==e or b==e: continue
                                if check[a] or check[b] or check[e]: continue
                                check[a], check[b], check[e] = True, True, True
                                f = B-b
                                if f == F-e and 1<=f<=13 and (not check[f]):
                                    cnt += 1
                                check[a], check[b], check[e] = False, False, False
                        check[i], check[j] = False, False
                        A, B = A+i, B+j
                    check[c], check[g] = False, False
                    E, F = E+c, F+g
                check[k] = False
                C, G = C+k, G+k
        check[m], check[l] = False, False
        A, B = A+l, B+m
    check[d], check[h] = False, False
    E, F = E+d, F+h
print(cnt)
