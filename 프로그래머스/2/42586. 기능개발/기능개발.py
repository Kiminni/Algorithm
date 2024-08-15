def solution(progresses, speeds):
    answer = []
    progress = 0
    speed = 0
    time = 0
    tmp = 0
    while len(progresses) > 0:
        if progresses[0] + speeds[0] * time >= 100:
            tmp += 1
            progresses.pop(0)
            speeds.pop(0)
            continue
        else:
            if tmp != 0 :
                answer.append(tmp)
            tmp = 0
        time += 1
    answer.append(tmp)
    return answer
            