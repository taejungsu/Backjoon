import sys

scales = list(map(int, sys.stdin.readline().split()))
check = 0


for i in range(len(scales)-1):
    if scales[i] + 1 == scales[i+1]:
        check = 1
    elif scales[i] - 1 == scales[i+1]:
        check = 2
    else:
        check = 0
        break

if check == 0:
    print('mixed')
elif check == 1:
    print('ascending')
elif check == 2:
    print('descending')