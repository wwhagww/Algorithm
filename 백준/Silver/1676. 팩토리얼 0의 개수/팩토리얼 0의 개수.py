import sys; input=sys.stdin.readline
n = int(input())
num = 1
for i in range(2, n+1):
    num *= i
print(len(str(num)) - len(str(num).rstrip('0')))