n = int(input())
count = 0
stack = []
result = []
flag = True

for _ in range(n) :
    data = int(input())
    while count < data :
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == data :
        stack.pop()
        result.append('-')
    else :
        flag = False
        break

if flag == False :
    print("NO")
else :
    print('\n'.join(result))