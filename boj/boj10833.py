# t = int(input())
sum = 0
for _ in range(int(input())):
    s, a = map(int, input().split())
    sum += a % s

print(sum)
