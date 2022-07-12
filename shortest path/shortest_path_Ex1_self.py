# 미래도시

import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

X, K = map(int, input().split())

distance1 = [INF] * (N + 1)
distance2 = [INF] * (N + 1)

def dijkstra(distance, start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for b, c in graph[node]:
            cost = c + dist

            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, [cost, b])
    
    distance[start] = INF


        
dijkstra(distance1, 1)
dijkstra(distance2, K)


ANS = distance1[K] + distance2[X]

# print(distance1)
# print(distance2)
# print(distance1[K], distance2[X])

print(ANS if ANS < INF else -1)


# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 3



# =======



# 4 2
# 1 3
# 2 4
# 3 4

# -1