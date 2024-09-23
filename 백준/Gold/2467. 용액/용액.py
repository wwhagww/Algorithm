n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n-1

minAbsTotal = int(2e9)
res = None

while left < right:
    leftVal = arr[left]
    rightVal = arr[right]
    total = leftVal + rightVal
    absTotal = abs(total)
    if absTotal < minAbsTotal:
        minAbsTotal = absTotal
        res = (leftVal, rightVal)
    if total > 0:
        right -= 1
    elif total < 0:
        left += 1
    else: break
# print(minAbsTotal)
print(res[0], res[1])