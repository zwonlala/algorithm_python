from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = []
max_list = []
for i in range(n):
    temp_list = list(map(int, input().split()))
    graph.append(temp_list)
    max_list.append(max(temp_list))

max_val = max(max_list)




def bfs(graph, x, y, visited):
    queue = deque([])
    visited[x][y] = True
    queue.append((x, y))

    # ANS_CNT += 1

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            if graph[nx][ny] <= H:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))


ANS = []
for H in range(max_val):
    visited = [[False] * n for _ in range(n)] 

    dx = [0 ,0, 1, -1]
    dy = [1, -1, 0 ,0]

    ANS_CNT = 0

    for x in range(n):
        for y in range(n):
 
            if graph[x][y] <= H:
                continue
            if visited[x][y]:
                continue

            bfs(graph, x, y, visited)
            ANS_CNT += 1

            
    ANS.append(ANS_CNT)
    

print(max(ANS))




