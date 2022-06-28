from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)

dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]

def bfs(graph, start, visited, N, M):
    q = deque([])
    x, y = start
    visited[x][y] = 1
    q.appendleft(start)
        
    while q:
        cur = q.popleft()
        print(x, y, end=' ')
        x, y = cur
        VAL = visited[x][y]
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # if visited[nx][ny]:
            #     continue
            
            if graph[nx][ny] == 0:
                continue
            if not visited[nx][ny] == -1:
                continue
                
            visited[nx][ny] = VAL + 1
            q.append((nx, ny))

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    visited = [[-1] * M for _ in range(N)]
    
    bfs(maps, (0, 0), visited, N, M)
    
    # print(visited)
    
    return visited[N-1][M-1]