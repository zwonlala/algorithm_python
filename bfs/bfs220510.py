from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # unecessary? -> Nope.

    while queue:
        v = queue.popleft();
        # visited[v] = True
        print(v, end=' ')

        for next in graph[v]:
            if not visited[next]:
                visited[next] = True # this is my mistake...?
                queue.append(next)

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