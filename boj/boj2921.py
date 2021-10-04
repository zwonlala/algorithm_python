n = int(input())
sum = 3
for i in range(2, n+1):
    sum = sum + i * (i + 1) + i * (i + 1) / 2

print(int(sum))
