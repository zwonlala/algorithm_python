# 220628 18:48 ~ 


# 정확성 : 16 / 20 , 효율성 : 2 / 4 (시간초과 2개)
'''
def solution(phone_book):
    for idx, phone in enumerate(phone_book):
        for compare in phone_book[0: idx] + phone_book[idx + 1:]:
            if phone in compare:
                return False
    
    return True
'''


# ~ 19:27 
# 정확성 : 18 / 20 , 효율성 : 2 / 4 (시간초과 2개)
'''

def solution(phone_book):
    if len(phone_book) <= 1:
        return True
    
    hash = {}
    duplicatedKeySet = set([])
    for phone in phone_book:
        key = int(phone[0])
        if key in hash :
            hash[key] += [phone]
            duplicatedKeySet.add(key)
        else :
            hash[key] = [phone]
            
    duplicatedKeyList = list(duplicatedKeySet)
       
    if len(duplicatedKeyList) == 0:
        return True
    
    for dup in duplicatedKeyList:
        sortedList = sorted(hash[dup], key = len)
        print(sortedList)
        
        for idx, small in enumerate(sortedList):
            for big in sortedList[idx + 1:]:
                if small in big:
                    return False
        return True
'''       
        
    
    

# ~ 19:33
# 정확성 : 18 / 20 , 효율성 : 2 / 4 (시간초과 2개)
'''
def solution(phone_book):
    if len(phone_book) <= 1:
        return True
    
    hash = {}
    duplicatedKeySet = set([])
    for phone in phone_book:
        key = int(phone[0])
        if key in hash :
            hash[key] += [phone]
            duplicatedKeySet.add(key)
        else :
            hash[key] = [phone]
            
    duplicatedKeyList = list(duplicatedKeySet)
       
    if len(duplicatedKeyList) == 0:
        return True
    
    for dup in duplicatedKeyList:
        sortedList = sorted(hash[dup], key = len)
        # print(sortedList)
        
        for idx, small in enumerate(sortedList):
            for big in sortedList[idx + 1:]:
                # if small in big:
                #     return False
                if big.startswith(small):
                    return False
        return True
'''
    
    

# 모르겠어서 검색해서 풀음...
# https://velog.io/@ledcost/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-42577-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8-%EB%AA%A9%EB%A1%9D-level-2-%ED%95%B4%EC%8B%9C
# dict에서 get 으로 찾는게 O(1)이라 배열 쓰는것보다 효율적..

def solution(phone_book):
    answer = True
    
    phone_dict = {}
    for key in phone_book:
        phone_dict[key] = 1
    
    for phone_num in phone_dict:
        temp = ''
        for num in phone_num:
            temp += num

            if temp in phone_dict and temp != phone_num:
                answer = False
                return answer
    return answer