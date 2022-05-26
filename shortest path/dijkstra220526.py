# from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

visited = [False] * (n + 1)

distance = [INF] * (n + 1)

def get_shortest_node():
    index = 0
    shortest = INF

    for i in range(1, n + 1):
        if not visited[i] and distance[i] < shortest:
            shortest = distance[i]
            index = i

    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0

    for b, c in graph[start]:
        distance[b] = c

    for _ in range(n - 1): # n is right?
        cur = get_shortest_node()
        visited[cur] = True

        # b, c = graph[cur]
        for b, c in graph[cur]:
            cost = distance[cur] + c

            if cost < distance[b]:
                distance[b] = cost

dijkstra(start)

for i in range(1, n + 1):
    print('INFINITY' if distance[i] == INF else distance[i])


# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
