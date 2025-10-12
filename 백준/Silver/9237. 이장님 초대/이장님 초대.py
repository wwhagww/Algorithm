N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
lst2 = [i+v for i, v in enumerate(lst, start=1)]
print(max(lst2)+1)
