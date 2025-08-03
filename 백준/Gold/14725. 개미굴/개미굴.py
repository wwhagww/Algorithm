N = int(input())
arr = []
for _ in range(N):
    line = input().split()
    arr.append(line[1:])
arr.sort()
prev = []
for line in arr:
    len_prev = len(prev)
    need_check = True
    for idx, word in enumerate(line):
        if idx < len_prev and need_check:
            if word == prev[idx]: continue
            else: need_check = False
        print("--"*idx+word)
    prev = line