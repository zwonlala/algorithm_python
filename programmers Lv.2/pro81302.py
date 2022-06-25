# 220625 14:34 ~

# 1try. ~ 15:03. 정확성 31/ 32
'''
from collections import deque

dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]

def dfs(graph, start):
    visited = [[False] * 5 for _ in range(5)]
    queue = deque([])
    
    x, y = start
    
    visited[x][y] = True
    queue.append(start)
    distance = 0
    
    for _ in range(2):
        if len(queue) == 0:
            break;
        cur = queue.pop()
        x, y = cur
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            
            if visited[nx][ny]:
                continue
            
            if graph[nx][ny] == 'X':
                continue
            elif graph[nx][ny] == 'O':
                visited[nx][ny] = True
                queue.append((nx, ny))
            elif graph[nx][ny] == 'P':
                return False
    return True
    

def solution(places):
    answer = []
    for place in places:
        place_str = ''.join(place)
        is_safe = True
        
        for idx, ch in enumerate(place_str):
            if ch == 'P':
                x = idx // 5
                y = idx % 5
                res = dfs(place, (x, y))
                if res == False:
                    is_safe = False
                    break
        if is_safe:
            answer.append(1)
        else:
            answer.append(0)
         
    return answer
'''



# 2try. 도저히 모르겠어서 검색해서 풀음....
# https://velog.io/@savannah030/programmers-81302-2021-%EC%9D%B8%ED%84%B4%EC%89%BD-2%EB%B2%88-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0

from collections import deque

dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]

def dfs(graph, start):
    visited = [[False] * 5 for _ in range(5)]
    queue = deque([])
    
    x, y = start
    
    visited[x][y] = True
    queue.append((x, y, 0))
    distance = 0
    
    while queue:
        x, y, cnt = queue.pop()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            
            if visited[nx][ny]:
                continue
            
            if graph[nx][ny] == 'X':
                continue
            if cnt > 2: continue
            
            elif graph[nx][ny] == 'O':
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))
            elif graph[nx][ny] == 'P' and cnt < 2:
                return False
    return True
    

def solution(places):
    answer = []
    for place in places:
        place_str = ''.join(place)
        is_safe = True
        
        for idx, ch in enumerate(place_str):
            if ch == 'P':
                x = idx // 5
                y = idx % 5
                res = dfs(place, (x, y))
                if res == False:
                    is_safe = False
                    break
        if is_safe:
            answer.append(1)
        else:
            answer.append(0)     
    return answer