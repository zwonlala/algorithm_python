# 220623 솔루션

import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville) # heapify: 리스트를 바로 heap화 해주는 함수
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0: # 위에가장 작은 요소 정답 아니었는데, len 값이 0이면, 아까 팝한 원소가 마지막 원소이니 실패함
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer