import sys
from collections import deque
 
n,m = map(int,sys.stdin.readline().split())
array=[[] for _ in range(n)]
 
for i in range(n):
    str = sys.stdin.readline().strip()
    for j in range(m):
        array[i].append(int(str[j]))
 
d = [[1,0],[0,1],[-1,0],[0,-1]]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    while queue:
        y1,x1 = queue.popleft()
        for dx,dy in d:
            if 0<=y1+dy<n and 0<=x1+dx<m:
                if array[y1+dy][x1+dx]==1:
                    array[y1+dy][x1+dx]=array[y1][x1]+1
                    queue.append((y1+dy,x1+dx))

bfs(0,0)
print(array[n-1][m-1])