# 송지원. 만약 문자열을 한 글자씩 나눠 저장하고 싶다면 다음과 같이 간단히 list로 Casting하기만 하면 된다.
li = list(input())
print(''.join(sorted(li, reverse=True)))

# print(''.join(sorted(list(input()), reverse=True)))
# 한줄 간단 가능