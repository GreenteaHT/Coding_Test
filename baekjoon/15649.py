import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
list0 = [i+1 for i in range(N)]
list1 = list(permutations(list0, M))
for k in list1:
    for j in k:
        print(j, end=' ')
    print()