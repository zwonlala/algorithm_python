n = int(input())
move = dict([
    ('L', [0, -1]),
    ('R', [0, +1]),
    ('U', [-1, 0]),
    ('D', [+1, 0])
])

move_list = input().split()

x = 1
y = 1

for m in move_list:
    dx, dy = move.get(m)
    # print(m, dx, dy)
    nx = x + dx
    ny = y + dy

    if nx <= 0 or nx > n or ny <= 0 or ny > n:
        continue
    x = nx
    y = ny

print(x, y)