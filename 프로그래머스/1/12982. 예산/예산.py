def solution(d, budget):
    answer = 0
    d.sort()
    tmp = budget
    for i in d:
        tmp = tmp - i
        if tmp < 0 :
            continue
        else:
            answer += 1
    return answer