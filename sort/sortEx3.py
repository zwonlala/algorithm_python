N, K = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort(reverse=True)

# print(arrA)
# print(arrB)

'''
for i in range(K):
    # print(arrA[i], arrB[i])
    arrA[i] = arrB[i]
'''

# 틀렸음.. 최대 K회 변경이 가능하니, B 배열이 A 보다 클 경우에만 바꿔치기 해야 함...!

for i in range(K):
    if arrA[i] < arrB[i]:
        arrA[i], arrB[i] = arrB[i], arrA[i]
    else:
        break

print(sum(arrA))
