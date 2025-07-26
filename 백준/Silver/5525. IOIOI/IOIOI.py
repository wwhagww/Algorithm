def count_ioi(arr, n):
    prev = arr[0]
    cnt = 0
    check = 0
    for cur in arr[1:]:
        if cur == "I":
            if prev == "O":
                if check >= n:
                    cnt += 1
            else: check = 0
        elif cur == "O":
            if prev == "I":
                check += 1
            else: check = 0
        prev = cur
        # print(cur, check, cnt)
    return cnt

N = int(input())
_ = input()
arr = input()
print(count_ioi(arr, N))