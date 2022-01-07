t = int(input())
for _ in range(t):
    li = sorted(list(map(int, input().split())))[1:4]
    print(sum(li) if ((li[-1] - li[0]) < 4) else 'KIN')
