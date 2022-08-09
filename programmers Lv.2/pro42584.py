# 220807 19:47 ~ 20:55

# 1st TRY. 효율성 생각 안하고 그냥 생각나는 대로 구현함... 정확성 1 / 10, 효율성 0 / 5
'''
def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        p = prices[i]
                
        cnt = 0
        for next in prices[i + 1:]:
            if p > next:
                break
            cnt += 1
        
        print(i, p, prices[i + 1:], cnt)

        answer.append(max(cnt, 1))
    answer[-1] = 0
        
    return answer
'''

# 모르겠어서 검색해서 풀음..
from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer