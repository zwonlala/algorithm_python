fib = [0] * 95;
fib[0] = 0
fib[1] = 1

n = int(input())
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]
print(fib[n]);