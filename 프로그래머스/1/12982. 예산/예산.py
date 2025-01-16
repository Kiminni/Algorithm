def solution(d, budget):
    d.sort()
    tmp = budget
    answer = 0
    for i in d:
        tmp = tmp - i
        if tmp >= 0:
            answer += 1
        else:
            break
    return answer