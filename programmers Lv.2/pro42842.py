# 220801 2234 ~ 23:17.... 개졸리다....
# 220802 19:42 ~ 아래 코드 실제 돌려보니 1케이스 틀림...! ~ 20:09

'''
brown = int(input())
yellow = int(input())

# def solution(brown, yellow):
whSum = (brown + 4) // 2
# whMul = (yellow - 4) + x2 * whSum
whMul = brown + yellow

for w in range(whMul, 1, -1):
    h = whSum - w;

    if h <= 2 or w <= 2:
        continue

    print(w, h, whMul % h, whMul % w)
    if whMul % h == 0 and whMul % w == 0 and  w >= h:
        print('hehehehe')
        break;
    
    # if w >= h:
    #     break;
        
    # return [w, h];
print([w, h])

'''



# 220802 어제 작성한대로 제출한 버젼 => 12 / 13 맞음!
def solution(brown, yellow):
    whSum = (brown + 4) // 2
    whMul = brown + yellow

    for w in range(whMul, 1, -1):
        h = whSum - w;

        if h <= 2 or w <= 2:
            continue

        if whMul % h == 0 and whMul % w == 0 and  w >= h:
            return [w, h]
    


# 220802 All Sol version.
def solution(brown, yellow):
    whSum = (brown + 4) // 2
    whMul = brown + yellow

    for w in range(whMul//3, 2, -1):
        h = whSum - w;

        if h <= 2 or w <= 2:
            continue

        if whMul % h == 0 and whMul % w == 0 and w*h == whMul and  w >= h:
            return [w, h]
    
