# 220611

# 1 try
# - 정확성 5 / 16
# - 효율성 0 / 5

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