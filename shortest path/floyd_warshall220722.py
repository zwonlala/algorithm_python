import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for x in range(N+1):
    graph[x][x] = 0

for k in range(1, N + 1):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for x in range(1, N + 1):
    for y in range(1, N + 1):
        print(graph[x][y], end=' ')
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
