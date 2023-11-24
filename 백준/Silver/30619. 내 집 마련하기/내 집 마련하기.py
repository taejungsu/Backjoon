import sys

def func():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    for i in range(M):
        L, R = map(int, sys.stdin.readline().split())

        now = L

        for j in range(N):
            if L <= A[j] <= R:
                sys.stdout.write(str(now) + " ")
                now += 1
            else:
                sys.stdout.write(str(A[j]) + " ")
        sys.stdout.write("\n")
func()


