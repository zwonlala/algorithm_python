array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]

        # 앞에는 이미 다 정렬되어있으므로, 위 조건에 맞지 않으면 나머지 반복문 돌 필요 없음
        else:
            break;

print(array)
        