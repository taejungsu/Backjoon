import sys

T = int(sys.stdin.readline())
result = [0] * T

for i in range(T):
    result[i] = int(sys.stdin.readline())

result.sort(reverse=True)

print(*result, sep='\n')