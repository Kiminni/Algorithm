def solution(s):
    ans_p = 0
    ans_y = 0
    for i in s:
        if i == 'p' or i == 'P':
            ans_p += 1
        elif i == 'y' or i == 'Y':
            ans_y += 1
    
    if ans_p == ans_y :
        return True
    
    return False