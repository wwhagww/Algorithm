N = int(input())
res = 0
for i in range(2, 10):
    if N==1 or N%i==0 and N < i*10:
        res = 1
        break
print(res)