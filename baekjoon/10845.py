import sys
n = int(sys.stdin.readline())
queue = []

for i in range(n):
    L = list(sys.stdin.readline().split())
    if L[0] == "push":
        queue.append(int(L[1]))
    elif L[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif L[0] == "size":
        print(len(queue))
    elif L[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif L[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif L[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])