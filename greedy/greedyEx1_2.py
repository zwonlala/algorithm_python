n, m, k = list(map(int, input().split()))
# print(n, m, k);
arr = list(map(int, input().split()))
biggest = max(arr)
# print(biggest)
biggestIdx = arr.index(biggest)

# second = max(arr[0, biggestIdx] + arr[biggestIdx:])
# secondIdx = arr.index(second)
# print(second, secondIdx)

arr.pop(biggestIdx)

second = max(arr)

print(biggest * (m // k) * k + second * (m % k))
