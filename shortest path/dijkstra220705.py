import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())

start = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (N + 1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if dist > distance[node]:
            continue

        for b, c in graph[node]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

    
dijkstra(start)

for i in range(1, N + 1):
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