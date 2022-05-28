# 220528 19:08 ~ 19:57

import sys
from collections import deque
from tracemalloc import start
input = sys.stdin.readline

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
# visited = [[False] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            # print(x, y)
            graph[y][x] = -1

# print(graph)

dx = [-1, 0, +1, 0]
dy = [0, -1, 0, +1]

def bfs(graph, start):
    queue = deque([])
    x, y = start
    current_sum = 1
    graph[y][x] = current_sum
    queue.append(start)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            # print(nx, ny)
            if graph[ny][nx] != 0:
                continue

            current_sum += 1
            graph[ny][nx] = current_sum
            queue.append((nx, ny))
        
    return current_sum

ANS = []
for x in range(n):
    for y in range(m):
        if graph[y][x] == 0:
            # print('<', str(x), ', ', str(y))
            size = bfs(graph, (x, y))
            # print(graph)
            ANS.append(size)

ANS = sorted(ANS)
STR_ANS = map(str, ANS)
print(len(ANS))
print(' '.join(STR_ANS))





