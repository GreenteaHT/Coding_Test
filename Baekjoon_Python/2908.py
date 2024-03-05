import sys
a, b = map(int, sys.stdin.readline().split())
a = a//100 + ((a//10)%10)*10 + (a%10)*100
b = b//100 + ((b//10)%10)*10 + (b%10)*100
print(max(a, b))