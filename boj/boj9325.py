for _ in range(int(input())):
    car = int(input())
    opt = 0
    cnt = int(input())
    for _ in range(cnt):
        q, p = map(int, input().split())
        opt += q * p
    print(car + opt)