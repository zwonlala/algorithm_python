# 220527 18:24 ~ 18:44

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([])
    visited[start] = True
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)


t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for __ in range(n + 1)]
    next = list(map(int, input().split()))
    for i in range(n):
        graph[i + 1].append(next[i])
    
    # print(n)
    # print(graph)
    visited = [False] * (n + 1)

    ANS = 0

    for i in range(1, n + 1):
        if not visited[i]:
            bfs(graph, i, visited)
            ANS += 1
    print(ANS)

