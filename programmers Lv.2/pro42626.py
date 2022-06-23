# 220623 22:00 ~ 



# 기존 코드..
'''
def makeNewScoville(arr):
    l1 = arr[0]
    l2 = arr[1]
    new = l1 + 2 * l2
    
    return [new] + arr[2:]

def solution(scoville, K):
    answer = 0
    
    while True:
        lowest = min(scoville)
        
        if lowest >= K:
            return answer
        
        if len(scoville) == 1 and lowest < K:
            return -1
        
        sorted(scoville)
        
        scoville = makeNewScoville(scoville)
        answer += 1
        
    return answer
'''


# 220623 푼거..
#  정확성 12/16 (57.1), 효율성 5/5 (23.8)
import heapq

def solution(scoville, K):
    ANS = 0
    
    q = []
    
    for s in scoville:
        heapq.heappush(q, (s, s))
    
    while True:
        min1, _ = heapq.heappop(q)
        if min1 >= K:
            break
        
        min2, _ = heapq.heappop(q)
        new = min1 + 2 * min2
        heapq.heappush(q, (new, new))
        ANS += 1
    return ANS
    
   


# 220623 2nd solution -> SOL!
import heapq

def solution(scoville, K):  
    if len(scoville) == 0:
        return 0
    ANS = 0
    q = []
    
    for s in scoville:
        heapq.heappush(q, (s, s))
    
    while True:
        # print(q)
        if len(q) < 2:
            return ANS if q[0][0] >= K else -1 # 이 부분이 문제였다...!
        
        min1, _ = heapq.heappop(q)
        if min1 >= K:
            break
        
        min2, _ = heapq.heappop(q)
        new = min1 + 2 * min2
        heapq.heappush(q, (new, new))
        ANS += 1
    return ANS