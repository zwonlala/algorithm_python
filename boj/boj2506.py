input()
arr = list(map(int, input().split()))
# print(arr)
sum, stack = 0, 0
for i in arr:
    stack = 0 if (i == 0) else stack + 1
    # print(i, stack)
    sum += stack
print(sum)