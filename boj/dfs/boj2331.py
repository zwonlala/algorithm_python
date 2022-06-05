# 220605 18:39 ~ 18:57 1솔 합

def get_multiple_sum(x, pow):
    sum = 0
    while x != 0:
        temp_x = x % 10
        x //= 10
        sum += temp_x ** pow
    return sum

a, p = map(int, input().split())

arr = [a]
recent = set([])
recent.add(a)

while True:
    a = get_multiple_sum(a, p)
    if not a in recent:
        arr.append(a)
        recent.add(a)
    else :
        print(arr.index(a))
        break
