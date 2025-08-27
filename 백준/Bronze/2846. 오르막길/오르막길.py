N = int(input())
arr = list(map(int, input().split()))
prev = arr[0]
st = arr[0]
max_gap = 0
for n in arr:
    if n <= prev:
        max_gap = max(max_gap, prev - st)
        st = n
    prev = n
else:
    max_gap = max(max_gap, prev - st)
print(max_gap)