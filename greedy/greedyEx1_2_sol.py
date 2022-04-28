# 교재 코드
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
big = data[-1];
second = data[-2];
print(big, second)

count = (m // (k + 1)) * k;
count += m % (k + 1);

print(count)

result = big * count + second * (m - count);
print(result)

# 5 8 3
# 2 4 5 4 6
