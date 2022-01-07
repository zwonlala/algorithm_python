n = int(input())
li = []
for _ in range(n):
    # 송지원 Python 리스트 원소 추가
    li.append(int(input()))

# print(li)
li = sorted(li)
# 송지원 python 문자열로 합치기
print('\n'.join([str(x) for x in li]))