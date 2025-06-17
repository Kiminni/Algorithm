def solution(progresses, speeds):
    answer = []
    time = 0
    progress = 0
    speed = 0
    tmp = 0
    
    while len(progresses) > 0:
        if progresses[0] + time * speeds[0] >= 100:
            tmp += 1
            speeds.pop(0)
            progresses.pop(0)
            continue
        else:
            time += 1
        
        if tmp:
            answer.append(tmp)
            tmp = 0
        
    answer.append(tmp)
    return answer
        