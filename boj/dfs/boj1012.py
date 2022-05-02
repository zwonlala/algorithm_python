#  220502 20:49 ~ 21:57....런타임 에러 나는데 모르겠어서 검색해서 풀음...
# 아래 두줄 추가해서 런타임 에러 해결...

import sys
sys.setrecursionlimit(10000)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [ [0] * m for i1 in range(n)]
    visited = [ [False] * m for i2 in range(n)]

    # print(graph)
    # print(visited)
    for i3 in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # print(graph)
    # print(visited)

    def dfs(graph, visited, x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False

        if graph[y][x] != 1:
            return False
        else :
            if not visited[y][x]:
                visited[y][x] = True

                dfs(graph, visited, x-1, y)
                dfs(graph, visited, x, y-1)
                dfs(graph, visited, x+1, y)
                dfs(graph, visited, x, y+1)

                return True
            return False
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(graph, visited, j, i):
                cnt += 1
    print(cnt)
