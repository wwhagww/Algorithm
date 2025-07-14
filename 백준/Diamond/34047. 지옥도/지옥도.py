def f(x, y, i):
  return min(i-x%i, x%i) % y

def check2(n, m, x, y):
  for i in range(1, int(n**0.5)+1): ###
    if f(n, m, i) != f(x, y, i):
      return False
  for i in range(1, int(n**0.5)+1):
    if f(n, m, n//i) != f(x, y, n//i):
      return False
    if f(n, m, n//i+1) != f(x, y, n//i+1):
      return False
  return True

K = 10**9

def solve(n, m):
  if m == 1:
    return (0, 1)
  if n <= K//2:
    if m > n: x, y = n, n + 1
    else: x, y = n, m
  else:
    y = max(K - n, n // 3)
    if m > y: x, y = n, y + 1
    elif m==2 and check2(n, m, n-2, m):
      x, y = n-2, m
    else: x, y = n, m
  return (x, y)

n, m = map(int, input().split())
x, y = solve(n, m)
print(x, y)
