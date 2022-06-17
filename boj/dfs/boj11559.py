# 220611 16:36 ~ 
# 220617 21:36 ~ 22:26

from collections import deque
import sys

input = sys.stdin.readline

X = 6
Y = 12

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(graph, start, visited):
    x, y = start
    KEY = graph[x][y]

    queue = deque([])
    visited[x][y] = True
    queue.append(start)

    node_to_delete = [start]

    while queue: 
        cur = queue.popleft()
        x, y = cur

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                continue
        
            if visited[nx][ny] == True:
                continue

            if graph[nx][ny] != KEY:
                continue

            node_to_delete.append((nx, ny))
            visited[nx][ny] = True
            queue.append((nx, ny))
    
    if len(node_to_delete) >= 4:
        for x, y in node_to_delete:
            graph[x][y] = '.'

        return True
    else :
        return False


def down(graph):
    for x in range(X):
        row = graph[x]
        next_row = []
        for cur in row:
            if cur != '.':
                next_row.append(cur)
        next_row = next_row + ['.'] * (Y - len(next_row))

        graph[x] = next_row



graph = [[0] * Y for _ in range(X)]

for y in range(Y):
    temp_str = input()

    for x in range(X):
        graph[x][11-y] = temp_str[x]


ANS = 0
while True:
    is_popped = False
    visited = [[False] * Y for _ in range(X)]
    for x in range(X):
        for y in range(Y):
            if not visited[x][y] and graph[x][y] != '.':
                is_popped |= bfs(graph, (x, y), visited)
    if is_popped:
        ANS += 1
        down(graph)
    else:
        break;

print(ANS)

    
