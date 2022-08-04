# 220804 19:45 ~ 20:27... 도저히 점화식 모르겠어서 검색해서 풀음..

def solution(n):
    answer = 0
    DIV =  1000000007
    
    if n % 2 == 1:
        return answer
    else:
        answer = 3
        answer_temp = answer
        a_sum = 1
        
        m = n // 2
        for i in range(m - 1):
            answer_temp = answer
            answer = (answer * 3 + a_sum * 2) % DIV
            a_sum += answer_temp
    
        return answer