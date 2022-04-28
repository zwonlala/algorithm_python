n, m = map(int, input().split())
arr = []

for _ in range(n):
    subArr = list(map(int, input().split()))
    arr.append(subArr)
# print(arr);

print(max(list(map(min, arr))))


# 3 3
# 3 1 2 
# 4 1 4
# 2 2 2 


# 2 4
# 7 3 1 8
# 3 3 3 4