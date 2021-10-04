n = int(input())
fib = [0] * 50
fib[1] = 1
fib[2] = 1

for i in range(3, n + 1):
    fib[i] = fib[i-1] + fib[i-2]
print(fib[n])
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55(10), 89, 144, 233, 377, 610, 987, 1597

