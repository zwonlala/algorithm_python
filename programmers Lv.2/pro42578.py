def solution(clothes):
    cloDict = {}
    for clo in clothes:
        value, key = clo
        if key in cloDict:
            cloDict[key].append(value)
        else:
            cloDict[key] = [value]
            
    if len(cloDict.items()) == 1:
        for values in cloDict.values():
            return len(values)
        
    ANS = 1
    for key, lists in cloDict.items():
        print(key, lists)
        ANS *= (len(lists) + 1)
    ANS -= 1
    return ANS
    