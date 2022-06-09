# 220609 21:16 ~ 1트 하다가 도저히 감이 안잡혀서 솔류션 검색해서 풂

# import sys
# sys.setrecursionlimit(10 ** 6)

# input = sys.stdin.readline

# def is_correct(arr):
#     for i in range(3):
#         for j in range(3):
#             ANS = 3 * i + j + 1

#             if ANS == 9:
#                 ANS = 0

#             if arr[i][j] != ANS:
#                 return False
#     return True

# def dfs(arr, position, cnt):


# arr = []
# for _ in range(3):
#     arr.append(list(map(int, input().split())))



""" 솔류션 보고 2트... 하지만 key 값을 2차원 배열로 하면서 시간 초과 뜸...
from collections import deque
import copy

def toString(arr):
    ANS = ''
    for i in range(3):
        for j in range(3):
            ANS += str(arr[i][j])
    return ANS

def getZeroPosition(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                return (i, j)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def getNextArr(arr):
    ANS = []
    zx, zy = getZeroPosition(arr)

    for d in range(4):
        nx = zx + dx[d]
        ny = zy + dy[d]

        if nx < 0 or nx > 2 or ny < 0 or ny > 2:
            continue

        nextVal = arr[nx][ny]
        tempArr = copy.deepcopy(arr)

        tempArr[zx][zy] = nextVal
        tempArr[nx][ny] = 0
        ANS.append(tempArr)
    return ANS

def isANS(arr):
    return toString(arr) == '123456780'

def bfs(arr, visited):
    queue = deque([])
    visited.add(toString(arr))
    queue.append((arr, 0))

    while queue:
        curArr, CNT = queue.popleft()

        if (isANS(curArr)):
            return CNT

        for nextArr in getNextArr(curArr):
            if toString(nextArr) in visited:
                continue

            queue.append((nextArr, CNT + 1))
            visited.add(toString(nextArr))
    
    return -1

arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

visited = set()

ANS = bfs(arr, visited)
print(ANS)

"""



from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def getNextArrayStr(str):
    STRS = []
    zeroIdx = str.index('0')
    zx = zeroIdx // 3
    zy = zeroIdx % 3

    for d in range(4):
        nx = zx + dx[d]
        ny = zy + dy[d]
        nIdx = 3 * nx + ny

        if nx < 0 or nx > 2 or ny < 0 or ny > 2:
            continue

        temp = list(str)
        temp[zeroIdx], temp[nIdx] = temp[nIdx], temp[zeroIdx]
        STRS.append(''.join(temp))
    return STRS

def isANS(str):
    return str == '123456780'

def bfs(str):
    queue = deque([])
    visited = set()
    visited.add(str)
    queue.append((str, 0))

    while queue:
        curStr, curCnt = queue.popleft()

        if (isANS(curStr)):
            return curCnt

        for next in getNextArrayStr(curStr):
            if next in visited:
                continue

            visited.add(next)
            queue.append((next, curCnt + 1))
    return -1

STR = ''
for _ in range(3):
    STR += ''.join(list(map(str, input().split())))
ANS = bfs(STR)
print(ANS)




