N, M = map(int, input().split())

coins = []
for _ in range(N):
    c = int(input())
    coins.append(c)

CNT = [-1] * (10001)

for c in coins:
    CNT[c] = 1

for i in range(1, M + 1):
    if i in coins:
        continue

    combinations = []
    for c in coins:
        if i - c > 0 and CNT[i - c] != -1:
            combinations.append(CNT[i - c] + 1)

    print(combinations)
    
    CNT[i] = min(combinations) if len(combinations) > 0 else -1

print(CNT[M])
# print(CNT)
        
