# 송지원 조금 더 pythonic 하게 짜기

def sum(n):
    sum = 0
    a = 1;
    while (n > 0):
        if (n > a):
            sum += a**2
            n -= a
        else :
            sum += n * a
            n = 0
        a+=1
    return sum

a, b = map(int, input().split())
# print(a);
# print(b);
print(sum(b) - sum(a-1));
