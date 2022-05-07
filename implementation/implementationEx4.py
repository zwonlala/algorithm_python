# n, m = map(int, input().split())
# x, y, d = map(int, input().split())

# gamemap = []
# for _ in range(n):
#     gamemap.append(list(map(int, input().split())))

# # print(gamemap)

# def getLeft(d):
#     directionMap = dict(
#         (1, 0),
#         (2, 1),
#         (3, 2),
#         (0, 3)
#     );
#     return directionMap.get(d)

# dx = [-1, 0, +1, 0]
# dy = [0, +1, 0, -1]

# cnt = 0

# def canMove(x, y, d):
#     direction = [0, 3, 2, 1]
#     for i in range(4):
#         curD = (3 + d - i) % 3
#         print(curD)
#         nx = x + dx[curD]
#         ny = y + dy[curD]

#         # print(nx, ny)

#         if gamemap[nx][ny] == 0:
#             return (nx, ny, curD)
#     return None

# while True:
#     moveResult = canMove(x, y, d)

#     if moveResult is None:
#         x -= dx[d]
#         y -= dy[d]
#         cnt += 1
#     else :
#         nx, ny, nd = moveResult
#         gamemap[nx][ny] = -1
#         cnt += 1
#         x = nx
#         y = ny
#         d = nd



n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    
count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 1회전 후 갈 수 있는 방법을 찾았을 때
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx;
        y = ny;
        count += 1
        turn_time = 0
        continue
    # 1회전 후 갈 수  없을 경우
    else:
        turn_time += 1

    # 4번 모두 회전 한 경우. 갈 수 있는 방법을 못 찾은 경우.
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 뒤로 가기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)



