# https://school.programmers.co.kr/learn/courses/30/lessons/181949

# 모르겠어서 검색해서 품.

s = input()
for ch in s:
    if ch.isupper() :
        print(ch.lower(), end='')
    else:
        print(ch.upper(), end='')



# 다른 사람 풀이

print(input().swapcase())


