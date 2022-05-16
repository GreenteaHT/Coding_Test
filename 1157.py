import sys
import collections
n = sys.stdin.readline().upper()
lst = collections.Counter(n)
del(lst['\n'])
a = [k for k,v in lst.items() if max(lst.values()) == v]
if len(a) > 1 and len(n) > 2:
    print("?")
else:
    print(a[0])

# 나중에 알고리즘 한번더