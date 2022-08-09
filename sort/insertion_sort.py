# 삽입 정렬
# O(N ^ 2)
# best case(거의 다 정렬되어있는 경우) : O( N )
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 1 부터 도는 이유는 왼쪽은 이미 정렬된 상태로 가정하여 두번째 요소 부터 돌기 때문
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

    
print(array)
