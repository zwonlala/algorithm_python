# 19:22 ~ 

# 1st try
'''
import sys
input = sys.stdin.readline

def get_key_list(p, q):
    strList = []
    for idx, token in enumerate(q):
        if idx == 4:
            break
            
        if token == '-':
            strList.append('ALL')
        else:
            strList.append(p[idx])
    return map(str, strList)
    

def solution(info, query):
    answer = []

    people = list(x.split(' ') for x in info)
    # print(people)
    queries = list(x.split(' and ') for x in query)
    scores = list(x.split(' ')[-1] for x in query)
    # print(queries)
    for q in queries:
        print()
        cnt = 0
        
        q_key = ' '.join(q[: -1]).replace('-', 'ALL')
        q_key += ' ' + q[-1].split(' ')[0].replace('-', 'ALL')
        
        q_list = q_key.split(' ')
        print(q_list)
        
        q_score = int(q[-1].split(' ')[1])
        # print(q_key)
        
        for p in people:
            keyList = get_key_list(p, q)
            # print(key)
            score = int(p[-1])
            
            
            
            # print(key, '/', q_key, '//', score, '/', q_score)
            
            # if q_key == key and score >= q_score:
            #     cnt += 1
        answer.append(cnt)
        
                                
    return answer
'''




# 

from collections import defaultdict

def solution(info, query):
    group_info = defaultdict(list)

    for idx, user_info in enumerate(info):
        lang, task, exp, food, score = user_info.split()
        score = int(score)

        case_list = []
        for a in ['-', lang]:
            for b in ['-', task]:
                for c in ['-', exp]:
                    for d in ['-', food]:
                        group_info[(a, b, c, d)].append(score)

    for key in group_info.keys():
        group_info[key].sort()       

    answer = []
    for q in query:
        lang, _, task, _, exp, _, food, score = q.split()
        score = int(score)

        temp = group_info[(lang, task, exp, food)]

        start, end = 0, len(temp) - 1
        while start <= end:
            mid = (start + end) // 2

            if temp[mid] < score:
                start = mid + 1
            else:
                end = mid - 1

        answer.append(len(temp) - start)
    return answer