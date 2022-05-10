# 220510 22:38 ~ 23:25

from collections import deque
import sys

input = sys.stdin.readline

def dfs(graph, i, visited):
    visited[i] = True
    print(i, end=' ')

    for next in graph[i]:
        if not visited[next]:
            dfs(graph, next, visited)


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for next in graph[v]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# graph의 각 리스트 정렬해야 함!!!
for i in range(n + 1):
    sorted_list = graph[i].sort()

visitedD = [False] * (n + 1)
visitedB = [False] * (n + 1)

dfs(graph, v, visitedD)
print()
bfs(graph, v, visitedB)

