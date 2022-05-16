import sys
count = 0
max = 0
for _ in range(9):
    count += 1
    a = int(sys.stdin.readline())
    if a > max:
        max = a
        index = count
print(max)
print(index)