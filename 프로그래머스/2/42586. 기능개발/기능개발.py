'''
1. progresses의 길이가 0일때까지 반복 -> 맨 첫번째 요소가 100을 넘을 때까지
2. 100을 넘으면 count 추가
3. 그렇지 않으면 count 0으로 변경, 
'''

def solution(progresses, speeds):
    time = 0
    speed = 0
    count = 0
    answer = []
    
    while(len(progresses) > 0):
        if progresses[0] + speeds[0] * time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0 :
                answer.append(count)
                count = 0
            else:
                time += 1
    
    answer.append(count)
    return answer
            
