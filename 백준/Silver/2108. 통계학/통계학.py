import sys
from collections import Counter
n = int(input())
a = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])
print(round(sum(a)/(l:=len(a))))
print(a[l//2])
s = sorted((Counter(a).items()), key = lambda x: (-x[1], x[0]))
if (len(s) == 1):
    print(s[0][0])
elif s[0][1] != s[1][1]:
    print(s[0][0])
else: print(s[1][0])
print(a[-1] - a[0])