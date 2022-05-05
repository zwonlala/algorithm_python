from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')

    while queue:
        # print(queue, end=' ')
        v = queue.popleft()
        # print(v, end=' ')

        # visited[v] = True //visited 처리를 여기가 아닌, 넣을 때 해야함!
        # print(v, visited, end='//')
        # print()

        for next in graph[v]:
            if not visited[next]:
                # visited[next] = True
                # print(visited)

                visited[next] = True # visited 처리는 넣을 때 해야함!
                print(next, end=' ')

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


