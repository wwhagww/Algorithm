year = 1
while True:
    inp = input()
    if inp == "0": break
    n, order = inp.split()
    words = []
    dct = {}
    for i, c in enumerate(order):
        dct[c] = i+1
    for _ in range(int(n)):
        words.append(input())
    print("year", year)
    for word in sorted(words, key=lambda x: tuple([dct[c] for c in x])):
        print(word)
    year += 1   