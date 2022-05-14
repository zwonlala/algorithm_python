# input 함수 재정의
import sys
input = sys.stdin.readline

# INF 정의
INF = int(1e9)

# 노드 수, 간선 수 입력
n, m = map(int, input().split())

# 시작 index 입력
start = int(input())

# graph, visited, shortest 정의
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

visited = [False] * (n + 1)

shortest = [INF] * (n + 1)

# 아직 방문하지 않은 노드들 중 가장 작은 노드번호 리턴하는 함수 구현
def get_shortest_node():
    index = 0
    shortest_val = INF

    for i in range(1, n + 1):
        if not visited[i]:
            if shortest[i] < shortest_val:
                shortest_val = shortest[i]
                index = i

    return index

# 다익스트라 알고리즘 구현
def dijkstra(start):
    visited[start] = True
    shortest[start] = 0
    for b, c in graph[start]:
        shortest[b] = c
    
    for _ in range(m):
        cur = get_shortest_node()
        visited[cur] = True
        
        for next in graph[cur]:
            b, c = next
            cost = shortest[cur] + c
            if cost < shortest[b]:
                shortest[b] = cost

dijkstra(start)

for i in range(1, n+1):
    print('INFINITY' if shortest[i] == INF else shortest[i])


