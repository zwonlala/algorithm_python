# 22:45 ~ 23:14

import heapq

INF = int(1e9)

def dijkstra(graph, distance, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        
        if dist > distance[node]:
            continue
            
        for b, c in graph[node]:
            cost = dist + c
            
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))
                
def binary_search(data, target):
    data.sort()
    start = 0
    end = len(data) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        # if data[mid] == target:
        #     return mid
        if data[mid] <= target:
            start = mid + 1
        else: 
            end = mid - 1
    return start
    # return None

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    distance = [INF] * (N + 1)
    
    dijkstra(graph, distance, 1)
    
    print(sorted(distance[1: ]))
    
    idx = binary_search(sorted(distance[1: ]), K)

    
    return idx
    
    
        
        
   