import queue
def solution(k, score):
    hall = []
    answer = []
    for s in score:
        if len(hall) < k:
            hall.append(s)
            hall = sorted(hall, reverse=True)
            answer.append(hall[-1])
        
        elif len(hall) == k:
            hall.append(s)
            hall = sorted(hall, reverse=True)
            hall.pop()
            answer.append(hall[-1])
        
    return answer