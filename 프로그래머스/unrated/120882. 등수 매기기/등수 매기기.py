def solution(score):
    answer = []
    tmp = []
    for i in range(len(score)):
        tmp.append(sum(score[i]) / len(score[i]))
    
    sort_tmp = sorted(tmp, reverse=True)
    
    for i in tmp:
        answer.append(sort_tmp.index(i) + 1)
    
    
    return answer