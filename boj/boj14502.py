# 220621 19:21 ~ 고민하다가 모르겠어서 검색함.
# 19:51 ~ 20:12 개념서 다시 봄
# 20:12 ~ 20:47 sol...

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

dx = [-1, 0, +1, 0]
dy = [0, -1, 0, +1]

def bfs(graph, viruses, visited, wallls):
    temp_graph = copy.deepcopy(graph)

    for wx, wy in wallls:
        temp_graph[wx][wy] = 1

    queue = deque([])

    for x, y in viruses:
        visited[x][y] = True
        queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visited[nx][ny]:
                continue

            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    CNT = 0

    for row in temp_graph:
        CNT += row.count(0)
                
    return CNT

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

viruses = []
blank = []
for x in range(N):
    for y in range(M):
        if graph[x][y] == 2:
            viruses.append((x, y))
        if graph[x][y] == 0:
            blank.append((x, y))

ANS = 0

for com in combinations(blank, 3):
    # print(com)
    visited = [[False] * M for _ in range(N)]
    temp_ANS = bfs(graph, viruses, visited, com)
    if temp_ANS > ANS:
        ANS = temp_ANS

print(ANS)


