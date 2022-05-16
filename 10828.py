import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    L = list(sys.stdin.readline().split())
    if L[0] == "push":
        stack.append(int(L[1]))
    elif L[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    elif L[0] == "size":
        print(len(stack))
    elif L[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif L[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])