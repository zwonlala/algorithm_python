# 220729 22:34 ~ 
# 220801 모르겠어서 해설 보고 풀음..


from collections import deque

def solution(people, limit):
    answer = 0
    sorted_limit = sorted(people)
    q = deque(sorted_limit)
    
    while q:
        minVal = q[0]
        maxVal = q[-1]
        
        if len(q) == 1:
            answer += 1
            q.pop()
            continue
        
        if minVal + maxVal <= limit:
            answer += 1
            q.popleft()
            q.pop()
        else:
            answer += 1
            q.pop()
            
    return answer