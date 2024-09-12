n = int(input())
st = set()
for _ in range(n):
    line = input()
    words = line.split()
    for idx, word in enumerate(words):
        c = word[0].upper()
        if c not in st:
            st.add(c)
            print(" ".join(words[:idx]+[f"[{word[0]}]{word[1:]}"]+words[idx+1:]))
            break
    else:
        for i, c in enumerate(line):
            if c == " ": continue
            c = c.upper()
            if c not in st:
                st.add(c)
                print(f"{line[:i]}[{line[i]}]{line[i+1:]}")
                break
        else: print(line)