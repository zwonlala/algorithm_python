# 퀵 정렬 python 간단 ver.
# O ( N log N)
# worst case: 다 정렬되어있는 경우 ..

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나의 원소만 가지고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # pivot은 첫번째 원소
    tail = array[1: ] # pivot 제외한 나머지 원소들을 tail 로 정의

    left_side = [x for x in tail if x <= pivot] # pivot 보다 작은 원소들 왼쪽으로
    right_side = [x for x in tail if x > pivot] # pivot 보다 큰 원소들 오른쪽으로

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))