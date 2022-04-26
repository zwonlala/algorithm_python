def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0) # count()라는 함수가 있다!!! 담엔 이거 쓰기!
    ans = 0 # 이런 방식으로도 겹치는 요소 비교가 가능하다!! 이게 더 직관적이고 실수할 확률이 낮은듯!
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]