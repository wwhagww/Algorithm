import sys; input=sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    a = n // 5
    b = n % 5
    print("++++ "*a + "|"*b)