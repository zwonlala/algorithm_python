# 220603 22:33 ~ 
# 도저히 모르겠어서 검색해서 품.. 23:00 ~
'''
def get12(circle):
    return circle[0]

def get3(circle):
    return circle[2]

def get9(circle):
    return circle[6]

def isN(circleNum):
    return circleNum == 0

def getPoint(circles):
    points = 0
    for idx, circle in enumerate(circles):
        points += (2 ** idx) * get12(circle)
    return points 

def getRotatable(circles):

def rotate(circles, position, direction):
'''

# https://inspirit941.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-14891-%ED%86%B1%EB%8B%88%EB%B0%94%ED%80%B4

import sys
from collections import deque

input = sys.stdin.readline

def check_right(start, dirs):
    if start > 4 or gears[start-1][2] == gears[start][6]:
        return
    
    # 오른쪽 확인
    if gears[start-1][2] != gears[start][6]:
        # 인접한 톱니바퀴가 회전 가능한지 파악
        check_right(start + 1, -dirs)
        gears[start].rotate(dirs)

def check_left(start, dirs):
    if start < 1 or gears[start][2] == gears[start+1][6]:
        return
    
    if gears[start + 1][6] != gears[start][2]:
        check_left(start -1, -dirs)
        gears[start].rotate(dirs)

gears = {}

for i in range(1, 5):
    gears[i] = deque(list(map(int, list(input().replace('\n', '')))))

n = int(input())
for _ in range(n):
    num, dirs = map(int, input().split())
    check_right(num + 1, -dirs)
    check_left(num - 1, -dirs)

    gears[num].rotate(dirs)

result = 0
for i in range(4):
    result += (2**i) * gears[i+1][0]
print(result)
