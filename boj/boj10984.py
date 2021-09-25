t = int(input())
for _ in range(t):
    gpa = .0
    sum = 0
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        sum += int(a)
        gpa += float(b) * float(a)
    print(sum, round(gpa / float(sum), 1))

# SyntaxError: cannot assign to literal
    gpa = .0, sum = 0
# 위 문장이 왜 신텍스 에러인지 검색하여 저장하기