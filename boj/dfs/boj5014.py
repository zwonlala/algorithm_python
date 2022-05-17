# 220517 21:15 ~ 21:37 1트 성공

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

f, s, g, u, d = map(int, input().split())

graph = [INF] * (f + 1)
visited = [False] * (f + 1)

def bfs(graph, start, u, d, visited):
    graph[start] = 0
    dy = [+u, -1 * d]

    queue = deque([])
    visited[start] = True
    queue.append(start)

    while queue:
        cur = queue.popleft()

        for i in range(2):
            next = cur + dy[i]

            if next <= 0 or next > f:
                continue

            if visited[next]:
                continue

            # if graph[next] > graph[cur] + 1:
            graph[next] = graph[cur] + 1
            visited[next] = True
            queue.append(next)

bfs(graph, s, u, d, visited)

# print(graph)

print(graph[g] if graph[g] != INF else 'use the stairs') 
            


