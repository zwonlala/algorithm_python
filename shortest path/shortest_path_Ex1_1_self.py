import sys
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for i in range(N):
    # graph[i][i] = INF # 이 부분 틀렸다...!
    graph[i][i] = 0


for k in range(1, N + 1):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

ANS = graph[1][K] + graph[K][X]

print(ANS if ANS < INF else -1)



# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 3



# =======



# 4 2
# 1 3
# 2 4
# 3 4

# -1