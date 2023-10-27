import sys

read = lambda: sys.stdin.readline().rstrip()

N, M = map(int, read().split())

A = list(map(int, read().split()))
B = list(map(int, read().split()))

answer = A + B
answer.sort()

print(*answer)