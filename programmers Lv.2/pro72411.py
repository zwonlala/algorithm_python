# 220624 22:09 ~ 


'''
function getComb(arr, n) {
    const result = [];
    if (n === 1) {
        return arr.map(item => [item]);
    }
    arr.forEach((fixed, i, array) => {
        const rest = array.slice(i + 1);
        const combs = getComb(rest, n - 1);
        const attached = combs
            .map(c => [fixed, ...c])
            .map(arr => arr.join(''));
        result.push(...attached);
    });
    return result;
}

function solution(orders, course) {
    var answer = [];
    const strMap = new Map();
    const MAX_LENGTH = course[course.length - 1];
    const orderCombinations = [];
    orders.forEach(order => {
        let combinations = []
        for (let length of course) {
            if (length <= order.length) {
                combinations = getComb([...order], length);                 
                // console.log(combinations);  
                orderCombinations.push(...combinations);
            }
        }
    });
    // console.log(orderCombinations);
    
    orderCombinations.forEach(combination => {
        strMap.has(combination) 
            ? strMap.set(combination, strMap.get(combination) + 1)
            : strMap.set(combination, 1);
    });
    // console.log(Array.from(strMap.entries()))
    const sortedOrderCombinations = Array.from(strMap.entries()).sort((a, b) => {
        return - (a[1] - b[1]);
    });
        
    console.log(sortedOrderCombinations);
    sortedOrderCombinations.forEach(([combination, count]) => {
        if (course.includes(combination.length) && count >= 2) {
            answer.push(combination);
        }
            
    })
    return answer;
}
'''


# 정확성 5/20
'''
from itertools import combinations

def solution(orders, course):
    answer = []
    
    collections = []
    for order in orders:
        for l in range(2, len(order) + 1):
            comb = combinations(order, l)
            collections += list(comb)    
    
    collectionsMap = {}
    collectionLenList = [0] * 12
    for collection in collections:
        collection_str = ''.join(sorted(collection))
        if collection_str in collectionsMap:
            collectionsMap[collection_str] += 1
        else :
            collectionsMap[collection_str] = 1
            
        str_len = len(collection)
        if collectionLenList[str_len] < collectionsMap[collection_str]:
            collectionLenList[str_len] = collectionsMap[collection_str]
    
    for key in collectionsMap:
        cnt = collectionsMap[key]
        
        if 2 <= cnt and cnt == collectionLenList[len(key)]:
            answer.append(key)

    return sorted(answer)
'''