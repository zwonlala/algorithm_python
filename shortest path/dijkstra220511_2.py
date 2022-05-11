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
def get_shortest_node():
    index = 0
    shortest = INF
    for i in range(n + 1):
        if not visited[i]:
            if distance[i] < shortest:
                shortest = distance[i]
                index = i
    return index


# 다익스트라 알고리즘

def dijkstra(start):
    visited[start] = True
    distance[start] = 0

    for j in graph[start]:
        b, c = j
        distance[b] = c
    
    for _ in range(n - 1):
        v = get_shortest_node()
        visited[v] = True

        for j in graph[v]:
            b, c = j
            cost = distance[v] + c

            if distance[b] > cost:
                distance[b] = cost

dijkstra(start);

for i in range(1, n+1):
    print("INFINITY" if distance[i] == INF else distance[i]) 








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