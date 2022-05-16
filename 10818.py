import sys
n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
print(min(L), max(L))