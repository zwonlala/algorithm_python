import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# input a number of Nodes and Edges
n, m = map(int, input().split())
# input a number of start Node
start = int(input())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

# input all edgs of graph
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            b, c = i
            cost = dist + c

            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

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