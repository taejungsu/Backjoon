N, M = map(int, input().split())
card_num = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i + 1, N):
        for z in range(j + 1, N):
            card_combi_sum = card_num[i] + card_num[j] + card_num[z]
            if card_combi_sum <= M:
                result = max(result, card_combi_sum)
                
print(result)