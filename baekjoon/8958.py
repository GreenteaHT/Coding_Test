import sys
n = int(sys.stdin.readline())

for _ in range(n):
    m = sys.stdin.readline()
    count = 0
    score = 0
    for i in range(len(m)):
        score += count
        if m[i]=="O":
            count += 1
        elif m[i]=="X":
            count = 0
    print(score)