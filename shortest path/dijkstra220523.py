# input 재정의
import sys
input = sys.stdin.readline

# 무한 정의
INF = int(1e9)

# 전체 노드 수, 엣지 수 입력
n, m = map(int, input().split())

# 시작 노드 입력
start = int(input())

# 그래프, 방문상태, 노드별 최단거리 리스트 입력
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

visited = [False] * (n + 1)

distance = [INF] * (n + 1)

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환

def get_smalleset_node():
    index = 0
    shortest_dist = INF

    for i in range(1, n + 1):
        # if not visited[i] and distance[i] < shortest_dist:
        #     shortest_dist = distance[i]
        #     index = i

        if distance[i] < shortest_dist and not visited[i]:
            shortest_dist = distance[i]
            index = i
    
    return index

# 다익스트라 알고리즘

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for b, c in graph[start]:
        distance[b] = c

    for _ in range(n - 1):
        cur = get_smalleset_node()
        visited[cur] = True

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