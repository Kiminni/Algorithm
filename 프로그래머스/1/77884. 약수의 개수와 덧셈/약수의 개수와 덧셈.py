def solution(left, right):
    answer = 0
    for idx in range(left, right + 1):
        
        tmp = 0
        for i in range(1,idx + 1):
            if idx % i == 0 :
                tmp += 1
                
        if tmp % 2 == 0:
            answer += idx
            
        else:
            answer -= idx
            
    return answer