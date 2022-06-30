from collections import deque

def bfs(graph, start, visited):
    q = deque([])
    visited[start] = True
    q.append(start)

    while q:
        cur = q.popleft()
        print(cur, end = ' ')

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

