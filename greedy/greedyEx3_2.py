n, k = map(int, input().split())
cnt = 0
while(n != 1):
    if (n % k == 0):
        # print(n, ' /')
        n //= k
        cnt += 1
    else:
        # print(n, ' -1')
        n -= 1
        cnt += 1
print(cnt)


# 25 5