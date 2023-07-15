string = input()

answer = "z" * len(string)

for i in range(1, len(string) - 1):
    for j in range(i + 1, len(string)):
        s1 = string[:i][::-1]
        s2 = string[i:j][::-1]
        s3 = string[j:][::-1]
        new_string = s1 + s2 + s3
        answer = min(answer, new_string) 

print(answer)