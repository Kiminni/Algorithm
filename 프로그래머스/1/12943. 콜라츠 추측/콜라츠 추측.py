def solution(num):
    if num == 1:
        return 0
    
    for i in range(500):
        if num == 1:
            return i
        
        if num % 2 == 0:
            num = num // 2
            
        elif num % 2 == 1:
            num = num * 3 + 1
            
    return -1