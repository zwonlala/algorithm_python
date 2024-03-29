# 220501 22:49 ~ 23:20 1트 틀림.
# 220502 20:32 ~ 20:41 솔.

n = int(input())
e = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(graph)


visited = [False] * (n + 1)

def dfs(graph, visited, i):
    if i < 0 or i > n:
        return 0
    
    if visited[i] == False:
        visited[i] = True
        print(i, graph[i]);
        for j in graph[i]:
            print(j, graph[i])
            dfs(graph, visited, j)

dfs(graph, visited, 1)

print(visited)
print(visited.count(True) - 1)
    



# 220502 2nd try

n = int(input())
e = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)

def dfs(graph, visited, i):
    if i < 0 or i > n:
        return 0
    
    if visited[i] == False:
        visited[i] = True
        for j in graph[i]:
            dfs(graph, visited, j)

dfs(graph, visited, 1)
print(visited.count(True) - 1)
    
