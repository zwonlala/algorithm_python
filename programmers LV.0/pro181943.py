# https://school.programmers.co.kr/learn/courses/30/lessons/181943


def solution(my_string, overwrite_string, s):
    res = str()
    start = s
    end = s + len(overwrite_string)
    for idx, ch in enumerate(my_string): # enumerate 기억이 안나서 검색해서 풀음.
        if start <= idx < end:
            res += overwrite_string[idx-start]
        else:
            res += ch
    return res
    

# py에서 배열의 idx 와 value 같이 불러오는 법

# 1. range() 사용하는 법
arr = [1, 3, 5]

for idx in range(len(arr)):
  print(idx, arr[idx])



# 2. enumerate() 내장 함수 사용하는 방법
arr = [2, 4, 6]

for idx, val in enumerate(arr):
  print(idx, val)



# 다른 사람 풀이

# 1. slicing 사용하는 방법!
#  - start, end 계산 없이 그냥 슬라이싱 쓰면 됐던 문제였다...!
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]