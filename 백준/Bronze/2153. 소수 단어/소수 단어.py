import math

word = input()

total = 0
for w in word:
    if w.islower():
        total += ord(w) - 96    # a : 97
    else:
        total += ord(w) - 38    # A : 65

isPrime = True
for i in range(2, int(math.sqrt(total)) + 1):
    if total % i == 0:
        isPrime = False

if isPrime:
    print('It is a prime word.')
else:
    print('It is not a prime word.')