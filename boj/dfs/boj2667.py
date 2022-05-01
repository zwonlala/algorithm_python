# 220501 22:33 ~ 22:47

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y>= n:
        return 0
    
    if graph[x][y] == 1:
        cnt = 1
        graph[x][y] = 0

        cnt += dfs(x-1, y)
        cnt += dfs(x, y-1)
        cnt += dfs(x+1, y)
        cnt += dfs(x, y+1)

        return cnt
    else :
        return 0

ans = []

for i in range(n):
    for j in range(n):
        cur_cnt = dfs(i, j)

        if cur_cnt != 0:
            ans.append(cur_cnt);
ans.sort()
print(len(ans))
for i in ans:
    print(i)