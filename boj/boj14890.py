# 220621 21:39 ~ 22:35 솔

import sys
input = sys.stdin.readline

def is_valid(arr, N, L):
    val = arr[0]
    same_cnt = 1
    check_cnt = 0
    used = [False] * N

    for i in range(1, N):
        if arr[i] == val:
            same_cnt += 1
            if check_cnt != 0:
                check_cnt -= 1
                used[i] = True
            continue

        diff = arr[i] - val

        if diff > 1:
            return False
        elif diff == 1:
            if check_cnt > 0:
                return False

            if same_cnt >= L:

                temp = False
                for j in range(i-L, i):
                    temp |= used[j]
                
                if temp == True:
                    return False

                val = arr[i]
                same_cnt = 1
                continue
            else :
                return False
        elif diff < -1:
            return False
        elif diff == -1:
            if check_cnt != 0:
                return False

            val = arr[i]
            same_cnt = 1
            check_cnt = L - 1
            used[i] = True
    
    if check_cnt == 0:
        return True
    else:
        return False


N, L = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
col_arr = []
for i in range(N):
    temp = list(map(lambda x: x[i], arr))
    col_arr.append(temp)

# print(arr)
# print(col_arr)

ANS = 0

for x in arr:
    print(x, is_valid(x, N, L))
    if is_valid(x, N, L):
        
        ANS += 1
for y in col_arr:
    print(y, is_valid(y, N, L))

    if is_valid(y, N, L):
        ANS += 1

print(ANS)


# print(is_valid([3, 2, 1, 1, 2, 3], 6, 1))
# print('=====')
# print(is_valid([3, 2, 2, 2, 3, 3], 6, 1))