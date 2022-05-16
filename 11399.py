n, k = map(int, input().split())
list0 = []
stack = 0
for i in range(n):
    list0.append(int(input()))
for j in range(n):
    stack += k//list0[n-j-1]
    k %= list0[n-j-1]
print(stack)
