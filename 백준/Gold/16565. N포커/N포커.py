from math import comb

N = int(input())
cnt = 0
for i in range(1, 14):
    if i*4 > N: break
    if i%2==1:
        cnt += comb(52-i*4, N - i*4) * comb(13, i)
    else:
        cnt -= comb(52-i*4, N - i*4) * comb(13, i)
    # print(i, cnt)
print(cnt%10007)
