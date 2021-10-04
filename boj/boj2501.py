n, k = map(int, (input().split()))
divArray = []

for i in range(1, n+1):
    if (n % i == 0):
        divArray.append(i)

print(0 if len(divArray) < k else divArray[k-1])