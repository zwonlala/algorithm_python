# -*- coding: utf-8 -*-

# 2020.10.31 18:13 ~
# page 92
# 큰 수의 법칙

n ,m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

count = m // (k + 1)
remain = m % (k + 1)

ANS = 0
ANS += numbers[-1] * count * k
ANS += numbers[-2] * count * 1
ANS += numbers[-1] * remain
print(ANS)


# <교재 코드>
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n - 1]
# second = data[n - 2]
#
# count = int(m / (k + 1)) * k
# count += m % (k + 1) # 마지막에 더해줄 가장 큰 수 더할 횟수
#
# result = 0
# result += (count) * first
# result += (m-count) * second #두번째로 큰 수를 한번씩 더하는 횟수는 전체 횟수(m)에서 가장 큰 수를 더하는 횟수(count)만큼을 뺀 차
#
# print(result)