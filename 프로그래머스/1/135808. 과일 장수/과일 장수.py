def solution(k, m, score):
    score = sorted(score, reverse = True)
    tmp = []
    answer = 0
    for i in range(len(score) // m):
        tmp = score[i * m :m * (i+1)]
        answer += min(tmp) * m
    return answer