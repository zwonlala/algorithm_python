from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    print(start, end= ' ')

    q = deque([start])
    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                print(next, end= ' ')
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