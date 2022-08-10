array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # for j in range(i + 1, 0, -1):
    for j in range(i, 0, -1):
        '''
        if i == 0 or array[j] < array[i]:
            array[i], array[j] = array[j], array[i]
        '''
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break
        

print(array)