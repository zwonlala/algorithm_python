array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

cnt = [0] * (max(array) + 1)

for x in array:
    cnt[x] += 1

for i in range(len(cnt)):
    if cnt[i] > 0:
        for _ in range(cnt[i]):
            print(i, end =' ')