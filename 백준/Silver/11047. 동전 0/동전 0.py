n,k = map(int,input().split())
a = []
coin = 0
for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)

for i in a:
    coin += k//i
    k = k%i
print(coin)