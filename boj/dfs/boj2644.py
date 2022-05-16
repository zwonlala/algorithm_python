# 220516 22:15 ~ 22:33 1트 틀림
#        22:33 ~ 22:44 모르겠어서 검색해서 솔...ㅎ

from collections import deque
import sys
input = sys.stdin.readline
NONE = -1

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visited = [NONE] * (n + 1)

def bfs(graph, start, visited):
    queue = deque([])
    visited[start] = 0
    queue.append(start)

    while queue:
        cur = queue.popleft()

        for next in graph[cur]:
            if visited[next] == NONE:
                visited[next] = visited[cur] + 1
                queue.append(next)

bfs(graph, a, visited)

# print(visited)
print(visited[b])

