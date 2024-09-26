n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0

curSum = 0
curLen = 0

minLen = n + 1

while True:
    if curSum >= s:
        minLen = min(minLen, curLen)
        if left < right:
            curSum -= arr[left]
            curLen -= 1
            left += 1
        else: break
    else:
        if right < n: 
            curSum += arr[right]
            curLen += 1
            right += 1
        else: break

if minLen > n:
    print(0)
else:
    print(minLen)