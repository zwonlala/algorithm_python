# arr = list(map(int, input().split()))
arr = []
dic = {}

for _ in range(10):
    i = int(input())
    arr.append(i)

    if i in dic.keys():
        dic[i] = dic[i] + 1
    else :
        dic[i] = 1
    # 위 if / else 문으로 작성한 부분 더 pythonic 하게 짤 순 없나...?

# print(arr)
# print(dic)

print(max(arr)//10)
print(max(dic.values()))