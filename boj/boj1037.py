n = int(input())
li = list(map(int, input().split()))

li = sorted(li)
print(li[0]**2 if len(li) == 1 else li[0]*li[-1])