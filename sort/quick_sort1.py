# 퀵 정렬
# O ( N log N)
# worst case: 다 정렬되어있는 경우 ..

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start

    left = start + 1
    right = end

    while left <= right:
        
        # left
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # right
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # left, right 엇 갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)