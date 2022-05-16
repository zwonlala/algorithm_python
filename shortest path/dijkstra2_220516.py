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

distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이 라인이 기존에 방문한 노드면 continue 시키는거 맞나...?
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