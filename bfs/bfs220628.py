from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)

def bfs(graph, start, visited):
    q = deque([])
    visited[start] = True
    q.appendleft(start)

    while q:
        cur = q.popleft()
        print(cur, end=' ')

        # if visited[cur]:
        #     continue

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)