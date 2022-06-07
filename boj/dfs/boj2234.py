# 220607 21:21 ~ 23:34 3번 빼고 풀음...

from collections import deque
import sys
input = sys.stdin.readline


dn = [-1, 0, 1, 0 ]
dm = [0, -1, 0, 1 ]

def get_direction(n):
    n = 15 - n
    d = [8, 4, 2, 1]
    direction = []
    for i in range(4):
        if n - d[i] >= 0:
            direction.append(3 - i)
            n -= d[i]

    return direction

def bfs(graph, start, visited):
    queue = deque([])
    queue.append(start)

    n, m = start 
    visited[m][n] = True
    CNT = 1

    while queue:
        n, m = queue.popleft()
        val = graph[m][n]

        for d in get_direction(val):
            nn = n + dn[d]
            nm = m + dm[d]

            if nn < 0 or nn >= N or nm < 0 or nm >= M:
                continue
            if visited[nm][nn]:
                continue

            visited[nm][nn] = True
            queue.append((nn, nm))
            CNT += 1
    return CNT

N, M = map(int, input().split())

graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))

visited = [[False] * (N) for _ in range(M)]

room_list = []
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            size = bfs(graph, (j, i), visited)
            room_list.append(size)

print(room_list)
room_list.sort()

print(len(room_list))
print(room_list[-1])
print(room_list[-1] + room_list[-2])
