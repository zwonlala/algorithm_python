# [프로그래머스] Greedy > 조이스틱 문제

<br>

- 문제 링크 : [프로그래머스 Level 2 조이스틱](https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3)

<br>

- 스스로 풀었는가 : X   
(생각한 풀이과정은 맞았으나 풀이과정을 코드로 옮기지 못함...)

<br>
<br>
<br>


## 소스코드

```python3
def solution(name):
    # name의 요소만큼 for를 돌면서, 해당 문자의 A에서부터 거리와, Z에서부터 거리 + 1 값 중 작은 값을 저장한 배열을 구한다.
    # 해당 배열의 값이 'A'에서부터 해당 알파벳까지 가기위한 최소 횟수임
    name_maker = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
 
    answer = 0
    # 0번부터 순회를 할꺼고
    idx = 0
    while True:
        answer += name_maker[idx]
        name_maker[idx] = 0
        
        # end condition. 배열의 모든값이 0이면, 모든 알파벳을 맞춘 상태이거나 나머지가 'A'로 채워진 상황이니
	# 더 이상 좌우로 이동하거나 'A'에서 특정 알파벳으로 가기 위해 위아래로 이동할 필요 없음
        if sum(name_maker) == 0:
            break;
        
        # 이 부분이 어떻게 구현해야 할지 모르겠던 부분.
        # left, right 값을 1부터 시작해서, 
        # index - left 번째, 
        # index + right 번째 name_maker 값이 0이 아닌 요소가 나올때까지의 값을 +1 씩하면서 돈다.
        # 이 left, right 값을 구하는 이유는 현재 위치에서 좌로 이동하는게 이득인지, 우로 이동하는게 이득인지 알아보기 위함.
        left, right = 1, 1
        while (name_maker[idx - left] == 0):
                left += 1
        while (name_maker[idx + right] == 0):
                right += 1
        
        # 이제 다음 위치로 이동해야 하니, left나 right중 더 가까운 위치로 이동하고
        answer += left if (left < right) else right
        # 다음 위치는 사용된 left, right만큼 더하거나 빼준다!
        # -left 인 이유는 index를 왼쪽으로 이동하면 index가 더 작아지니!
        idx += -left if (left < right) else right
    return answer

```

<br>


- 참고한 블로그 : [https://codingspooning.tistory.com/58](https://codingspooning.tistory.com/58)


<br>
<br>
<br>