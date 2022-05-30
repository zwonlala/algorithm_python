# 220606 19:06 ~

# import sys
# sys.setrecursionlimit(10 ** 6)

# INF = int(1e6)

# def dfs(graph, start, val):

#     for next in graph[x]:


# n, m = map(int, input().split())

# graph = [[] for _ in range(n)]
# visited = [[INF] * n for _ in range(n)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a - 1].append(b - 1)
#     graph[b - 1].append(a - 1)
#     visited[b - 1][a - 1] = 1
#     visited[b - 1][a - 1] = 1


import sys
input = sys.stdin.readline

INF = int(1e9)

def get_shortest_node(distance, visited, n):
    index = 0
    shortest = INF

    for i in range(1, n + 1):
        if not visited[i] and distance[i] < shortest:
            shortest = distance[i]
            index = i
    return index

def dijikstra(graph, distance, visited, n, start):
    visited[start] = True
    distance[start] = 0

    for b, c in graph[start]:
        distance[b] = c
    
    for _ in range(n):
        cur = get_shortest_node(distance, visited, n)
        visited[cur] = True

        for b, c in graph[cur]:
            cost = distance[cur] + c
            if distance[b] > cost:
                distance[b] = cost

    return sum(distance)

n, m = map(int, input().split())
ANS = []

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

for start in range(1, n + 1):
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    temp = dijikstra(graph, distance, visited, n, start)
    ANS.append(temp)

print(ANS.index(min(ANS)) + 1)


