a=(4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0)
b=("A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F")
dct = dict(zip(b,a))

num = 0
den = 0
for _ in range(20):
    _, a, b = input().split()
    if b=="P": continue
    num += dct[b]*float(a)
    den += float(a)
print(num/den)