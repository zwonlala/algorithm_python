from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    # print(start, end=' ')

    while queue:
        v = queue.popleft()

        # if visited[v]:
        #     continue

        visited[v] = True
        print(v, end=' ')

        for next in graph[v]:
            if not visited[next]:
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