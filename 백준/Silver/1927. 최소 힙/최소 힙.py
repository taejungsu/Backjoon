import sys
import heapq

n = int(sys.stdin.readline())
heap = [] # 배열

for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)