# 220808 21:03 ~ 힘들어서 집감..
# 220809 19:02 ~ 19:23


# 220809 ver. 정확성 4 / 14
# 26, 27 라인 추가 후 ALL SOL
def getOrderSkill(skill, skill_tree):
    ch = ''
    for sk in skill_tree:
        if sk in skill:
            ch += sk
    return ch
    

def solution(skill, skill_trees):
    answer = 0
    possible_skill = set([])
    
    for l in range(len(skill)):
        possible_skill.add(skill[0: l + 1])
        
    for tree in skill_trees:
        orderTree = getOrderSkill(skill, tree)

        # 아래 두줄 추가하고 나서 올솔
        if orderTree == '':
            answer += 1

        if orderTree in possible_skill:
            print(orderTree)
            answer += 1
    return answer