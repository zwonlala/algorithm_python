# [프로그래머스] Greedy > 큰 수 만들기 문제

<br>

- 문제 링크 : [프로그래머스 Level 2 큰 수 만들기](https://programmers.co.kr/learn/courses/30/lessons/42883)

<br>

- 스스로 풀었는가 : X(75%)   
(생각한대로 구현하였으나 75%만 맞음...)

<img display="block" margin="auto" width="70%" alt="내 풀이 결과.." src="https://user-images.githubusercontent.com/13375734/128342506-effd9621-a1df-45b7-89d6-4b558a7d986c.png">


<br>
<br>
<br>


## 내 소스코드 (75%)

```python3
# 입력받은 seq list에서 val보다 작은 값 중 가장 큰 값과 해당 값의 index를 구하여 리턴하는 함수
def max_lt(seq, val):
    max = -1
    index = -1
    length = len(seq)
    
    for i in range(length - 1, -1, -1):
        if (max <= seq[i] < val):
            max = seq[i]
            index = i
    return (max, index)


def solution(number, k):
    answer = ''
    # 먼저 입력받은 number를 int 형 리스트로 만들고
    numArr = list(map(int, list(number)))
    # 반복문때 사용될 maxVal 값을 (최대값 + 1)로 설정한다
    maxVal = max(numArr) + 1
    
    while (k != 0):
        # 이전
        maxVal, maxIndex = max_lt(numArr, maxVal)
        
        if maxIndex <= k:
            maxVal = max(numArr) + 1
            numArr = numArr[maxIndex: ]
            answer = answer + str(numArr.pop(0))            

            k -= maxIndex
              
    return answer + ''.join(map(str, numArr))

```

<br>
<br>
<br>


## 소스코드

```python3
def solution(number, k):
    stack = []
    
    for n in number:
        while stack and n > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
            
        stack.append(n)
        
    if k > 0:
        for i in range(k):
            stack.pop()
        
        
    return ''.join(stack)
```

- 참고한 블로그 : [https://velog.io/@dailyhyun/프로그래머스-큰-수-만들기](https://codingspooning.tistory.com/58)


<br>
<br>
<br>