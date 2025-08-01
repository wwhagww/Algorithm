num = input()
ln = len(num)
num = int(num)
cnt = [0]*10

tmp = 0
for i in range(ln):
    a, b = num // 10**(i+1), (num%10**(i+1)) // 10**i
    # print(a, b, "tmp:",tmp)
    for j in range(10):
        cnt[j] += a * 10**i
        if j < b:
            cnt[j] += 10**i
        if j == b:
            cnt[j] += tmp+1 if i > 0 else 1
    cnt[0] -= 10**i
    tmp += b*10**i 
    # print(cnt)
print(" ".join(map(str, cnt)))