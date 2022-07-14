N = int(input())
ans = [0] * 1001
ans[1] = 1
ans[2] = 3

for i in range(3, N + 1):
    ans[i] = 2 * ans[i - 2] + ans[i - 1]

print(ans[N] % 796796)


