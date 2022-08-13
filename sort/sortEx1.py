N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

print(' '.join(map(str, sorted(arr, reverse=True))))