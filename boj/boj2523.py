n = int(input())
for i in range(n-1):
    print(str('*' * (i+1)))
print(str('*' * n))
for i in range(n-1):
    print(str('*' * (n - 1 - i)))