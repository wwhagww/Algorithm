import sys
lines = sys.stdin.readlines()
for line in lines:
    while line.find("BUG") != -1:
        line = line.replace("BUG", "")
    sys.stdout.write(line)