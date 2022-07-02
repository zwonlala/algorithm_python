# 220702 익숙치 않아서 보고 침

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    graph[x][x] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for x in range(1, n + 1):
    for y in range(1, n + 1):
        print('INFINITY' if graph[x][y] == INF else graph[x][y], end = ' ')
    print()