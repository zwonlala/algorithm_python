# input 재정의
from math import dist
import sys
input = sys.stdin.readline

# 무한 정의
INF = int(1e9)

# 전체 노드 수, 엣지 수 입력
N, M = map(int, input().split())

# 시작 노드 입력
start = int(input())

# 그래프, 방문상태, 노드별 최단거리 리스트 입력
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    # graph.append(list(map(int, input().split())))
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

visited = [False] * (N + 1)

distance = [INF] * (N + 1)

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환

def get_shoretest_node():
    index = 0
    dist = INF

    for i in range(1, N + 1):
        if not visited[i]:
            if distance[i] < dist:
                index = i
                dist = distance[i]
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    visited[start] = True
    distance[start] = 0

    for b, c in graph[start]:
        distance[b] = c

    for _ in range(N):
        cur = get_shoretest_node()
        visited[cur] = True
        cost = distance[cur]

        for b, c in graph[cur]:
            if not visited[b] and distance[b] > cost + c:
                distance[b] = cost + c

dijkstra(1)

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