# 220708 금철 끝나고 헤드 벵잉하다가 못 품...
# 220709 점화식 착각해서 4 번째 케이스 까지 적어보고 품
def solution(n):
    a = 1
    b = 2
    c = -1
    
    for d in range(3, n + 1):
        c = b + a
        a = b
        b = c
        
    return c % 1000000007;