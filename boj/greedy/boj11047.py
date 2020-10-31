N, K = map(int, input().split())

coin_values = []
for _ in range(N):
    value = int(input())
    coin_values.append(value)
coin_values.sort(reverse=True)
# print(coin_values)

ANS = 0
for val in coin_values:
    if (K // val > 0):
        ANS += (K // val)
        K %= val

print(ANS)