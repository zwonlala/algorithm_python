# 220426 21:31 ~ 21:46 1 try


def solution(lottos, win_nums):
    order_arr = [6, 6, 5, 4, 3, 2, 1]; # 순위는 이렇게 구하면 편하다 👍. 변수명은 rank로 해도 괜찮을듯
    zero_cnt = len([l for l in lottos if l == 0]); # 특정 조건을 만족하는 요소만으로 이루어진 배열 구하는 법
    # print(zero_cnt);
    same_cnt = len(list(set(lottos) & set(win_nums))); # 합집합 연산자는 & 이고, 집합을 배열로 변활하려면 []로 묶는게 아닌 list()로 묶어야 함
    # print(set(lottos) & set(win_nums));
    # print(same_cnt);
    
    return [
        min(order_arr[same_cnt], order_arr[same_cnt + zero_cnt]),
        order_arr[same_cnt]
    ]
    
    