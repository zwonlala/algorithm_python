
def tiling(n):
    a, b = 0, 1
    for i in range(n): 
        a, b = b, a+b # 이렇게 하면 C 라는 변수 정의할 필요 없이 원하는 바 구현 가능
    b = int(str(b)[-5:])
    return b


print(tiling(25))



# 우아한 코드다
def solution(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, (a + b) % 1000000007 # 큰 값 할당할때, 이렇게 나머지 계산 해주면서 적용하면 overflow 막는 코드 구현 가능
    return b
