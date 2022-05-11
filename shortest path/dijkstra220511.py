import sys
input = sys.stdin.readline

# 무한대 정의
INF = 1e9

# 전체 노드 수, 엣지 수 입력받는다
n, m = map(int, input().split())

# 시작 노드 입력받는다
start = int(input())

# 그래프, 방문 상태, 노드별 최단 거리 리스트를 저장한다
    # 1. 그래프 -> 노드 수 + 1 개 만큼 만듬... ∵ 그래야 0 인덱스 처리하지 않아도 됨
    # a, b, c를 입력받는데, 시작 노드, 종점 노드, 노드간 코스트
        # 근데 graph[a] 에 추가하는 거 말고, graph[b]에는 추가할 필요 없나...?????
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    # 2. 방문상태(visited)
visited = [False] * (n + 1)
    # 3. 노드별 최단 거리 리스트
distance = [INF] * (n + 1)



# 그 다음 현재 방문하지 않은 노드 중에서 "가장 최단 거리가 짧은" 노드의 번호를 반환하는 함수 구현
def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(n + 1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i

    return index




# 그리고 대망의 다익스트라 알고리즘

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    
    for j in graph[start]:
        b, c = j
        distance[b] = c

    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            b, c = j
            cost = c + distance[now]

            if cost < distance[b]:
                distance[b] = cost

dijkstra(start)

for i in range(1, n + 1):
    print('INFINITY' if distance[i] == INF else distance[i])

