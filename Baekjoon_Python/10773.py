# https://www.acmicpc.net/problem/10773

from collections import deque

k = int(input())

lst = deque()
for _ in range(k):
    n = int(input())
    if not n and lst:
        lst.pop()
    else:
        lst.append(n)

print(sum(lst))