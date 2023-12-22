def solution(absolutes, signs):
    length = len(signs)
    answer = 0
    i = 0
    while i < length :
        if signs[i] == False:
            answer -= absolutes[i]
            
        else:
            answer += absolutes[i]
        i += 1
        
        
    
    return answer