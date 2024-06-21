def solution(progresses, speeds):
    time = 0
    count = 0
    answer = []
    while progresses:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0 :
                answer.append(count)
                count = 0
                time = 0
            else:
                time += 1
    answer.append(count)
    return answer
            