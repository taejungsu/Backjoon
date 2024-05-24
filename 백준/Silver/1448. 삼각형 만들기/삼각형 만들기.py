import sys
input = sys.stdin.readline

n = int(input())
nList = []
for i in range(n):
    nList.append(int(input()))

nList.sort(reverse=True)

for i in range(n-2):
    if nList[i] < nList[i+1] + nList[i+2]:
        print(nList[i] + nList[i+1] + nList[i+2])
        exit()
print(-1)