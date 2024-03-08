def solution(s):

    for i in s.lower():
        if 'a' <= i <= 'z':
            return False
        
    if len(s) != 4 and len(s) != 6:
        return False
    
    return True