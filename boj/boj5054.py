# 송지원 소팅 다시 정리
t = int(input())
for _ in range(t):
    n = int(input())
    location = list(map(int, input().split()))
    location.sort()
    sum = location[-1] - location[0]
    for i in range(n-1):
        sum += location[i+1] - location[i];
    print(sum)