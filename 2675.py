import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a = list(sys.stdin.readline().split())
    text = a[1]
    pt = ''
    for k in text:
        pt += k * int(a[0])
    print(pt)