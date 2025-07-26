T = int(input())
for _ in range(T):
    com = input()
    n = int(input())
    if n > 0:
        arr = list(map(int, input()[1:-1].split(sep=",")))
    else:
        _ = input()
        arr = []
    is_rev = False
    left, right = 0, n
    for c in com:
        if c == "R":
            is_rev = not is_rev
        elif c == "D":
            if is_rev:
                right -= 1
            else:
                left += 1
            if left > right:
                print("error")
                break
    else:
        res = arr[left:right]
        if is_rev: res = res[::-1]
        print( "["+",".join(map(str, res))+"]" )
