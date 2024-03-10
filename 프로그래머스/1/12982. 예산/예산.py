def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            return answer
        answer += 1
    return answer