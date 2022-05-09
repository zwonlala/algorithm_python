import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보 가지고 있는 리스트
visited = [False] * (n + 1) # 방문한 적이 있는지 체크하는 리스트
distance = [INF] * (n + 1) # 노드별 최단거리 테이블을 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환하는 함수
def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1, n + 1):
        # distance[i]가 가장 작은 값 중, i가 방문하지 않은 값
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
    
def dijkstra(start):
    # start Node 관련 초기화
    distance[start] = 0 # start Node는 거리 0이므로 0으로 설정
    visited[start] = True # start Node 부터 방문할꺼니, start Node 방문 처리
    # start Node에 (연결된 Node와 거리 값)을 받아와서 distance 리스트에 설정
    for j in graph[start]:
        b, c = j
        distance[b] = c
    # start Node 관련 초기화 끝

    # start Node 제외, 전체 n - 1 노드에 대해 반복을 진행
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 최단 거리 update 및 방문 처리 한다.
        now = get_smallest_node()
        visited[now] = True
        # 현재 Node(now)와 연결된 다른 노드를 확인
        for j in graph[now]:
            b, c = j
            # 현재 Node(now)까지의 거리 + 현재 Node(now)에서 다음 Node로 가는 거리(c) = 다음 Node의 최단거리(cost)
            cost = distance[now] + c
            if cost < distance[b]: # 기존 최단거리(distance[b]) 보다 위에서 계산한 최단거리(cost)가 더 짧다면, 업데이트 진행!
                distance[b] = cost

dijkstra(start)

# dijkstra 알고리즘이 종료된 후, start Node에서 각 Node로 가기 위한 최단거리 출력
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