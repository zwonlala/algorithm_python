# 220805 20:37 ~ 

# 1try.... 15/16 SOL...
def solution(citations):
    cursor = 0
    LEN = len(citations)
    sorted_ci = sorted(citations, reverse=True)
    
    for N in range(LEN, 0, -1):
        while cursor < LEN and sorted_ci[cursor] >= N:
            cursor += 1

        left = LEN - cursor
        print(N, cursor, left)

        
        if cursor >= N and left <= N:
            return N;
        print()


# 2nd try.... ALL SOL... ~ 21:36

def solution(citations):
    cursor = 0
    LEN = len(citations)
    sorted_ci = sorted(citations, reverse=True)
    
    for N in range(LEN, 0, -1):
        while cursor < LEN and sorted_ci[cursor] >= N:
            cursor += 1
            
        left = LEN - cursor
        
        if cursor >= N and left <= N:
            return N
    return 0
