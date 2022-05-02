# 220502 22:03 ~ 22:20 1트 시간초과...
#        22:20 ~ 22:37 sys.stdin.readline() 검색해서 해결...

import sys
sys.setrecursionlimit(10000)

n, e = map(int, sys.stdin.readline().split(' '))
graph = [[] for _ in range(n)]
visited = [False] * n;

for _ in range(e):
    v1, v2 = map(int, sys.stdin.readline().split(' '))
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

# print(graph)

def dfs(graph, visited, i):
    if visited[i] :
        return False
    else :
        visited[i] = True
        for j in graph[i]:
            dfs(graph, visited, j)
        return True

cnt = 0
for i in range(n):
    # print(i, visited)
    if dfs(graph, visited, i):
        cnt += 1
print(cnt)

