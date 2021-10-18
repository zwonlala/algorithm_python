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

print(sum(arr)//10)
# print(max(dic.values()))

# arr.sort(key=lambda x: x.value())
# print()
# print(arr)

# https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python
print(max(dic, key=dic.get))

# 검색해볼 것!
# 1. dict pythonic 하게 짜는 법
# 2. dict의 value를 기준으로 정렬하여 최대/최소 key 값 구하는 법 방금 위 코드가 최선인가..?