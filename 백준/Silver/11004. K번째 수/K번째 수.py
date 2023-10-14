import sys

N, K = map( int, sys.stdin.readline().split() )

data_list = list( map( int, sys.stdin.readline().split()))

sorted_data_list = sorted(data_list)

print(sorted_data_list[K-1])
