import sys
N = int(input())
print("swimming "*N)
sys.stdout.flush()
arr = input().split()
for s in arr:
    if s == "bowling":
        print("soccer", end=" ")
    else:
        print("bowling", end=" ")
else:
    print()
sys.stdout.flush()
