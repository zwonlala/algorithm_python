# 220522 21:16 ~ 21:51 sol!

from collections import deque
import sys

input = sys.stdin.readline

def get_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def can_reach(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return get_distance(x1, y1, x2, y2) <= 1000

def bfs(graph, start, visited):
    queue = deque([])
    visited[start] = True
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)



t = int(input())
for _ in range(t):
    n = int(input())
    points = []
    for __ in range(n + 2):
        x, y = map(int, input().split())
        points.append((x, y))

    graph = [[] for i in range(n + 2)]
    for i in range(n + 2):
        for j in range(n + 2):

            if i != j and can_reach(points[i], points[j]):
                graph[i].append(j)
    # print(graph)

    visited = [False] * (n + 2)

    bfs(graph, 0, visited)

    print('happy' if visited[-1] else 'sad')


