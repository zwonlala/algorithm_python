N = int(input())
arr = list(map(int, input().split()))

ANS = [0] * N

for i in range(N):
    if i < 2:
        ANS[i] = arr[i]
        continue
    
    ANS[i] = max(ANS[: i - 1]) + arr[i]

# print(max(ANS))
print(ANS)
