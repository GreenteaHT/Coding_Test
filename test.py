
N = int(input())
for _ in range(N):
    A = int(input())
    cnt = 0
    lst = map(int, input().split())
    for i in lst:
        if i % 2 == 1:
            cnt += 1
    print(cnt)
