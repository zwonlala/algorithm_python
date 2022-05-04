position = input()

x = int(position[1]) - 1
y = ord(position[0]) - ord('a')

dx = [-2, -2, -1, +1, +2, +2, -1, +1]
dy = [-1, +1, -2, -2, -1, +1, +2, +2]

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
        continue
    count += 1

print(count)