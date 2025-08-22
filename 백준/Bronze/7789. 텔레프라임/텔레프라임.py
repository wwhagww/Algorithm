import sys; input=sys.stdin.readline
N, M = input().split()
a = int(N)
b = int(M)*10**(len(N)) + a

def is_prime(n):
    if n%2==0: return False
    for m in range(3, int(n**0.5)+2):
        if n%m==0: return False
    return True

if is_prime(a) and is_prime(b):
    print("Yes")
else:
    print("No")