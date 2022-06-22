import sys
input = sys.stdin.readline
import heapq

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
        cost, cur = heapq.heappop(q)

        if distance[cur] < cost:
            continue

        for b, c in graph[cur]:
            if distance[b] > cost + c:
                distance[b] = cost + c
                heapq.heappush(q, (distance[b], b))

dijkstra(start) # 이걸 빼먹음..ㅎ

for i in range(1, N + 1):
    print('INFINITY' if distance[i] == INF else distance[i])





