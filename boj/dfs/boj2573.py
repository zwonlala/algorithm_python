# 220517 21:39 ~ 
# 220522 21:15 ~ 감이 안잡혀서 검색해서 풀음

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input().split()))

    