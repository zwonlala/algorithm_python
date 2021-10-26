# li = [];
# # 여기서 입력받을때 list comprehension 같은 걸로 우아하게 입력받을 순 없는지..?
# for i in range(5):
#     score = sum(list(map(int, input().split())));
#     li.append((i, score))
# # 여기서 최댓값과, 최댓값의 index를 구하는 우아한 방법?
# li.sort(key= lambda x: x[1])
# print(li[-1][0] + 1, li[-1][1]);


li = [];
for i in range(1, 6):
    score = sum(list(map(int, input().split())));
    li.append((i, score))
li.sort(key= lambda x: x[1])
print(li[-1][0], li[-1][1]);
