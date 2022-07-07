import sys
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
M = int(input())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    # for j in range(N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, N + 1):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])


for x in range(1, N + 1):
    for y in range(1, N + 1):
        print(graph[x][y], end=' ')
    print()

