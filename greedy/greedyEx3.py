# -*- coding: utf-8 -*-

# 2020.10.31 19:11 ~ 19:18
# page 99
# 1이 될 때까지

n, k = map(int, input().split())
count = 0;

while (n != 1):
    if (n % k == 0):
        count+=1
        n /= k # /= 연산의 결과물은 실수!!
        print(n);
    else:
        count+=1
        n -= 1
        print(n)

print(count)







# <교재 코드1>
# n, k = map(int, input().split())
# result = 0
#
# while n >= k:
#     while n%k != 0:
#         n -= 1
#         result += 1
#     n //= k # /= 쓰지 말고 //= 쓰기!
#     result += 1
#
# while n > 1:
#     n -= 1
#     result += 1
#
# print(result)


# <교재 코드2>
# n, k = map(int, input().split())
# result = 0
#
# while True:
#     #n이 k로 나눠떨어지는 수가 될때까지 -1을 하는데 한번에 하기!
#     target = (n // k) * k
#     result += (n - target) #한번에 빼는 -1(n-target)
#     n = target
#     #이제 n은 k의 배수이니 나눠줄 수 있음!
#
#     #더 이상 못 나눠주면 반복문 탈출
#     if n < k:
#         break;
#     result += 1
#     n //= k
#
# result += (n - 1) #이렇게 n < k 인 경우 남은 수를 더해줘야지 입력이 100억 이상의 굉장히 큰 수가 들어와도 시간 초과 등이 나지 않는다..!
# print(result)
