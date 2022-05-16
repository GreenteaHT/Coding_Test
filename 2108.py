import sys
n = int(sys.stdin.readline())
list0 = [0 for col in range(8001)]
list1 = []
avg = 0
max0 = -4000
max1 = 0
min0 = 4000
mid = 0
flag = 0

for i in range(n):
    a = int(sys.stdin.readline())
    list0[a+4000] += 1
    avg += a
    if a > max0:
        max0 = a
    if a < min0:
        min0 = a
print(round(avg/n))

for j in range(8001):
    mid += list0[j]
    if list0[j] >= max1:
        if list0[j] == max1:
            list1.append(j)
        else:
            list1 = [j]
            max1 = list0[j]
    if flag == 0 and mid >= ((n-1)/2+1):
        flag = 1
        print(j-4000)


if len(list1) >= 2:
    print(list1[1]-4000)
else:
    print(list1[0]-4000)

print(max0 - min0)