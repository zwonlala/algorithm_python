# train = [[0, 0, 0] for _ in range(10)]
train = []
for i in range(10):
    a, b = map(int, input().split())
    train.append([a, b, 0 if i != 0 else b]) # 여기서 i 값 삼항 연산자로 값 입력한 부분 반대로 넣음

# print(train)

# 이 문제 입력 한줄로 받는 법 알아보기!!

for i in range(1, 10):
    train[i][2] = train[i-1][2] - train[i][0] + train[i][1]
    # print(train[i][2])

# print((lambda x: x[2])(train)) # 2열이 아닌 2행을 리턴해보림 ㅠ
# print(max((lambda x: x[2])(train)))
print(max(
    map(
        (lambda x:x[2]), # 이렇게 map 써서 각 행?에 lambda 함수 설정해야 함!
        train)
))
