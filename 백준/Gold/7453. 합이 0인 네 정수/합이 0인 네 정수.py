N = int(input())
inp = list(zip(*[map(int, input().split()) for _ in range(N)]))
lst1 = sorted([n1 + n2 for n1 in inp[0] for n2 in inp[1]])
lst2 = sorted([n1 + n2 for n1 in inp[2] for n2 in inp[3]])

nlst1 = []
prev = None
cnt = 1
for n in lst1:
    if prev == n:
        cnt += 1
        continue
    if prev is not None: 
        nlst1.append((prev, cnt))
    prev = n
    cnt = 1
else: nlst1.append((prev, cnt))

nlst2 = []
prev = None
cnt = 1
for n in lst2:
    if prev == n:
        cnt += 1
        continue
    if prev is not None: 
        nlst2.append((prev, cnt))
    prev = n
    cnt = 1
else: nlst2.append((prev, cnt))

len1 = len(nlst1)
len2 = len(nlst2)

i1 = 0
i2 = len2 - 1
res = 0
while i1 < len1 and i2 >= 0:
    n1, cnt1 = nlst1[i1]
    n2, cnt2 = nlst2[i2]
    sm = n1 + n2
    if sm > 0:
        i2 -= 1
    elif sm < 0:
        i1 += 1
    else:
        res += cnt1 * cnt2
        i1 += 1
        i2 -= 1

print(res)