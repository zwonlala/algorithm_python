array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 배열 길이만큼 순회하면서 제일 작은 숫자를 찾을거임

    min_idx = i # 가장 작은 원소의 index

    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
        
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)