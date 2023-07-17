import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
list=deque([i+1 for i in range(n)])
print('<', end='')
for i in range(n):
    for j in range(k-1):
        list.append(list.popleft())
    print(list.popleft(), end='')
    if(i!=n-1):
        print(',', end=' ')
print('>')