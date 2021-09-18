import math
# x = int(input())
# print(x);
# y = x ** 0.5
# print(y)
# z = math.ceil(y)
# print(z)
# M = z

M = math.ceil(int(input()) ** 0.5)
N = int(int(input()) ** 0.5)
# print(M, N)
SUM = 0
if (M > N):
    print(-1)
else:
    for i in range(M, N + 1):
        # print(i)
        SUM += i ** 2
    print(SUM, M**2)