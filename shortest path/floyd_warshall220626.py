import sys
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
M = int(input())

# graph = [[INF] * M for _ in range(N)]
# index 계산한 필요 없이 바로 (N + 1) 크기로 정의한다
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# for i in range(N):
# 1 부터 N까지 임
for i in range(1, N + 1):
    graph[i][i] = 0

# 간선 정보를 1도 안받았다아아아아아아아ㅏ;;;
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 모두모두 1 부터 ~ N
# for k in range(N):
#     for x in range(N):
#         for y in range(N):
for k in range(1, N + 1):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

# 여기두 1 부터 N 
# for x in range(N):
#     for y in range(N):
for x in range(1, N + 1):
    for y in range(1, N + 1):
        print(graph[x][y] if not graph[x][y] == INF else "INFINITY", end=' ')

    print()
