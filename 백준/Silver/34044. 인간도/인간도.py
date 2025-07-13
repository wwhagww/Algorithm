# import itertools as it
# prm = [13, 17, 19, 23 ,29, 31, 37, 41, 43, 47, 53, \
#     59, 61, 67, 71, 73, 79, 83, 89, 97]
# det = [(n%10) - (n//10) if (n%10) - (n//10) >= 0 \
#     else (n%10) - (n//10) + 11 for n in prm]
# print(sorted(list(zip(det, prm))))

n = int(input())
if n == 1: print(-1)
elif n % 2 == 0: print("2343"*(n//2))
else: print("134343"+"2343"*(n//2-1))