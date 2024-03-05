
# def fibonacci(n):
#     if (n == 0):
#         return 0
#     elif (n == 1):
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
def fibonacci(n):
    list1 = [0, 1, 1]
    a = 1
    b = 1
    for i in range(40):
        a += b
        list1.append(a)
        c = a
        a = b
        b = c
    return list1[n]

L = int(input())
list0 = []
for j in range(L):
    list0.append(int(input()))
for i in list0:
    if i == 0:
        print("1 0")
    else:
        print(fibonacci(i-1), fibonacci(i))
