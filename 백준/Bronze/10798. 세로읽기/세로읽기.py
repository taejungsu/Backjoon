arr = []

for _ in range(5):
    a = input()
    arr.append(a)

for i in range(max(len(w) for w in arr)):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end="")