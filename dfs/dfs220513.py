def dfs(graph, i, visited):
    print(i, end=' ')
    visited[i] = True

    for next in graph[i]:
        if not visited[next]:
            dfs(graph, next, visited)

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

dfs(graph, 1, visited)
