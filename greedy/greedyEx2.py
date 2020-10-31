# -*- coding: utf-8 -*-

# 2020.10.31 18:43 ~ 19:03
# page 96
# 숫자 카드 게임

n, m = map(int, input().split())

data = []
for i in range(n):
    row = list(map(int, input().split())) #리스트.sort()의 리턴값은 None!!!
    row.sort()
    data.append(row)


minVals = [data[i][0] for i in range(n)] # 리스트 컴프리헨션 쓸 때는 넣고 싶은 걸 앞쪽에!
# minVals = []
# for i in range(n):
#     minVals.append(data[i][0])
# minVals.sort()

print(minVals[-1])






# <교재 코드1>
# n, m = map(int, input().split())
#
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
#
# print(result)




# <교재 코드2>
# n, m = map(int, input().split())
#
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = 10001
#     for a in data:
#         min_value = min(min_value, a)
#     result = max(result, min_value)
#
# print(result)
