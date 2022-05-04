def dfs(graph, i, visited):
    if visited[i]:
        return

    visited[i] = True
    print(i, end = ' ')

    for next in graph[i]:
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