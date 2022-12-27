# 220611 18:24 ~ 

from collections import deque
import sys

input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([])
    X, Y = start
    visited[x][y] = True
    queue.append(start)

    while queue:
        cur = queue.popleft()
        


N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))
print(graph)