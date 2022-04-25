
def solution(id_list, report, k):
    answer = [0] * len(id_list) # 입력으로 id 개수 만큼 0으로 초기화된 배열로 정답 배열 초기화
    reports = {x : 0 for x in id_list} # dict 하나를 정의할 건데, dict에 들어갈 값은 {x: 0} 그리고 x 값은 id_list 에 있는 값들로 구성함

    for r in set(report): # 문제 조건 속에 중복 제거한다고 나와 있으니, report를 중복 제거한 set(repot)를 순회하는데,
        reports[r.split()[1]] += 1 # 신고당한 사람(==="r.split()[1]") 을 key로 dict에 접근하여 값을 1 증가함. (=== 신고 1회 당함!)

    for r in set(report): # 다시 report를 중복 제거한 set(repot)를 순회
        if reports[r.split()[1]] >= k: # 위에서 구한 reports dict 의 현재 신고당한 사람(r.split()[1])의 카운트가 k 이상이면,
            answer[id_list.index(r.split()[0])] += 1 # 해당 신고자(r.split()[0])의 인덱스!!!! "id_list.index(r.split()[0])"에 접근하여 1 증가시킴

    return answer
