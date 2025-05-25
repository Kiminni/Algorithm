"""
1. 리스트를 높은 순으로 정렬
2. m개만큼의 사과만 먹고 분리
3. 최종적으로는 전체 이익을 리턴
"""
def solution(k, m, score):
    max_value = 0
    score = sorted(score, reverse=True)
    list_score = []
    tmp = []
    for i in range(len(score)):
        if len(tmp) < m:
            tmp.append(score[i])
        if len(tmp) == m:
            list_score.append(tmp)
            tmp = []
    
    if len(tmp) == m:
        list_score.append(tmp)
    
    for l in list_score:
        max_value += min(l) * m
    
    return max_value
        