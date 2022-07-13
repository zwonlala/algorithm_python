import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [INF] * (N + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if dist > distance[node]:
            continue

        for y, z in graph[node]:
            cost  = z + dist
            if cost < distance[y]:
                distance[y] = cost
                heapq.heappush(q, (cost, y))


dijkstra(C)

CNT = N - distance.count(INF) + 1
MAX = -1
for dis in distance:
    if dis >= INF:
        continue

    MAX = max(MAX, dis)

print(CNT, MAX)


# 3 2 1
# 1 2 4
# 1 3 2 

# 2 4