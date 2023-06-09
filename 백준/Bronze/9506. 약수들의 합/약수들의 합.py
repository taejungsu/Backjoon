while True:
    num_list = []
    total = 0
    n = int(input())
    
    if n == -1:
        break
    
    for i in range(1, n//2+1):
        if n % i == 0:
            num_list.append(i)
            total += i
            
    if total == n:
        temp = ' + '.join(str(i) for i in num_list)
        print(n, '=', temp)
    else:
        print('{} is NOT perfect.'.format(n))