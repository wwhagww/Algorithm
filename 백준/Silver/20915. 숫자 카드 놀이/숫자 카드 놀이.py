T = int(input())
for _ in range(T):
    arr = list(map(int, list(input())))
    for i in range(len(arr)):
        if arr[i] == 6: arr[i] = 9
    arr.sort(reverse=True)
    a, b = 0, 0
    for num in arr:
        if a <= b:
            a *= 10
            a += num
        else:
            b *= 10
            b += num
    print(a*b)
        