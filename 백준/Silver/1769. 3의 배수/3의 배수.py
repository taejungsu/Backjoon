n = input()
c=0
while int(n)>=10:
    t = 0
    for i in range(len(n)):
        t+=int(n[i])
    n=str(t)
    c+=1
print(c)
if int(n)%3==0:
    print("YES")
else:   
    print('NO')