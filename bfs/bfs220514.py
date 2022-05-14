from collections import deque

def bfs(graph, start, visited):
    queue = deque([])
    visited[start] = True
    queue.append(start)

    while queue:
        cur = queue.popleft()
        print(cur, end=' ')

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
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