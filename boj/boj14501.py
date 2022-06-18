# 220618 23:32 ~ 

import sys
input = sys.stdin.readline

N = int(input())

Arr = [[0] * N for _ in range(3)]
for i in range(N):
    a, b = map(int, input().split())
    Arr[0][i] = a
    Arr[1][i] = b


for i in range(N-1, -1, -1):
    # print('<<' + str(i))
    # print(Arr)
    # print(Arr[2])
    a = Arr[0][i]
    b = Arr[1][i]

    if (i + a) <= N:
        Arr[2][i] = b
        rest_arr = Arr[2][i + a:]
        if len(rest_arr) > 0:
            Arr[2][i] += max(rest_arr)

print(max(Arr[2]))
