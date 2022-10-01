# # 이 부분 틀림. deque 자료구조 import 해야 함
# from collections import deque

# # def bfs(graph, start, visited):
# #     if visited[start]:
# #         return

# #     visited[start] = True
# #     print(start, end=' ')

# #     for next in graph[start]:
# #         bfs(graph, next, visited)

# def bfs(graph, start, visited):

#     # bfs는 ~~ 자료구조를 사용하는 알고리즘 매커니즘
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')

#         for i in graph[v]:
#             if not visited[i]:
#                 # queue에 넣기 전에 이미 접근한 곳인지 판단한 후에 큐에 넣어준다!
#                 visited[i] = True
#                 queue.append(i)

# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9

# bfs(graph, 1, visited)



from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        cur = queue.popleft()
        #### # visited[cur] = True
        print(cur, end=' ')

        for next in graph[cur]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True


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