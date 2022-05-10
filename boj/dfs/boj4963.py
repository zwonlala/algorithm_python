# 330510 23:31 ~ 24:21

from collections import deque
import sys
input = sys.stdin.readline

dx = [0, +1, +1, +1, 0, -1, -1, -1]
dy = [-1, -1, 0, +1, +1, +1, 0, -1]

def bfs(graph, start, w, h, visited, island_cnt):
    X, Y = start
    if visited[Y][X]:
        return island_cnt
    if graph[Y][X] == 0:
        return island_cnt

    queue = deque([])
    visited[Y][X] = True
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        # print('<', x, '//', y, '>')

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            # print('((', nx, '/', ny, '))')

            if nx<0 or nx >= w or ny<0 or ny>=h:
                continue

            if graph[ny][nx] == 0:
                continue

            if visited[ny][nx]:
                continue

            visited[ny][nx] = True
            queue.append((nx, ny))

    return island_cnt + 1


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [[] for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int, input().split()))

    visited = [[False] * w for _ in range(h)]
    CNT = 0

    for x in range(w):
        for y in range(h):
            if graph[y][x] == 1 and not visited[y][x]:
                CNT = bfs(graph, (x, y), w, h, visited, CNT)
    
    print(CNT)

