for i in range(9):
    temp = list(map(int, input().split()))

    if i == 0:
        max_value = max(temp)
        row = i + 1
        col = temp.index(max_value) + 1

    else:
        if max_value < max(temp):
            max_value = max(temp)
            row = i + 1
            col = temp.index(max_value) + 1

print(max_value)
print(row, col)