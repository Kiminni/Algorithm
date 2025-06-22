def solution(progresses, speeds):
    answer = []
    time = 0
    progress = 0
    tmp = 0
    
    while progresses:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            tmp += 1
            continue
        
        else:
            time += 1
        
        if tmp > 0 :
            answer.append(tmp)
            tmp = 0
    answer.append(tmp)
    
    return answer
            
        