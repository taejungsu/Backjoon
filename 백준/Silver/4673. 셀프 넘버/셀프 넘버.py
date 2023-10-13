def d(n):
    num = list(str(n))
    asw = n
    for i in range(len(num)):
        asw += int(num[i])
    return asw

set = list(range(1,10001))
for n in range(1,10001):
    if d(n) in set:
        set.remove(d(n))
    
for i in range(len(set)):
    print(set[i])