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
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # for b, c in graph[start]:
    #     distance[b] = c

    while q:
        cost, node = heapq.heappop(q)

        if cost > distance[node]:
            continue

        for b, c in graph[node]:
            new_cost = cost + c
            if distance[b] > new_cost:
                distance[b] = new_cost
                heapq.heappush(q, (new_cost, b))

dijkstra(start)

for i in range(1, N + 1):
    print('INFINITY' if distance[i] == INF else distance[i])


