import sys
from collections import deque

N = int(input())
Queue = deque([])

for _ in range(N):
    line = sys.stdin.readline().split()

    if line[0] == "push":
        Queue.append(line[1])
    elif line[0] == "pop":
        if not Queue:
            print(-1)
        else:
            print(Queue.popleft())
    elif line[0] == "front":
        if len(Queue) > 0:
            print(Queue[0])
        else:
            print(-1)
    elif line[0] == "back":
        if len(Queue) > 0:
            print(Queue[-1])
        else:
            print(-1)
    elif line[0] == "size":
        print(len(Queue))
    elif line[0] == "empty":
        if len(Queue) > 0:
            print(0)
        else:
            print(1)