INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 리스트(그래프)를 만들고, 모든 값을 무한대로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에게 가는 비용은 0
for x in range(1, n + 1):
    graph[x][x] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
for k in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for x in range(1, n + 1):
    for y in range(1, n + 1):

        if graph[x][y] == INF:
            print("INFINITY", end = ' ')
        else:
            print(graph[x][y], end = ' ')
    print()


# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2