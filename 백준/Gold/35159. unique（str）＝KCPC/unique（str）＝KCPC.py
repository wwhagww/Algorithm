S = input()
pc = []
cnt_k = 0
res = 0
for idx, char in enumerate(S):
    if char == "K":
        res += idx - cnt_k
        cnt_k += 1
    else:
        pc.append(char)

res += pc.index("C")
pc.pop(pc.index("C"))

pc.reverse()
res += pc.index("C")
pc.pop(pc.index("C"))

L = len(pc)
cnt_p = 0
total_p = pc.count("P")
for char in pc:
    if char == "C":
        res += min(cnt_p, total_p - cnt_p)
    else:
        cnt_p += 1
print(res)