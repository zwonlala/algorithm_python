# 220806 19:36 ~ 19:42. ALL SOL.


def solution(s):
    str_len = len(s)
    # stack = []
    stack_len = 0
    
    for i in range(str_len):
        ch = s[i]
        
        if ch == '(':
            # stack.append()
            stack_len += 1
        else:
            stack_len -= 1
            
        if stack_len < 0:
            return False
        
    return stack_len == 0
        