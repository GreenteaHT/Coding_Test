import sys
n, k = map(int, sys.stdin.readline().split())
circle = [i for i in range(1, n+1)]
yo = []

count = k-1

while len(circle) != 0:
    len_c = len(circle)
    while len_c > count:
        yo.append(circle[count])
        circle[count] = 0
        count += k
    count %= len_c
    while 0 in circle:
        circle.remove(0)
print("<", end='')
print(*yo, sep = ', ', end='')
print(">", end='')

#오세푸스 문제