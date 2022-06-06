import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# visited = [False] * (n + 1) // version 2 don't need "visited" Arr
distance = [INF] * (n + 1)

def dijkstra2(start):
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

dijkstra2(start)

for i in range(1, n + 1):
    print('INFINITY' if distance[i] == INF else distance[i]) 
