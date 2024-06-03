'''
1. progresses의 길이가 0일때까지 반복 -> 맨 첫번째 요소가 100을 넘을 때까지
2. 100을 넘으면 count 추가
3. 그렇지 않으면 count 0으로 변경, 
'''
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while (len(progresses) > 0) :
        if progresses[0] + time * speeds[0] >= 100 :
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        
        else:
            if count > 0 :
                answer.append(count)
                count = 0
            time += 1
        
    answer.append(count)
    return answer