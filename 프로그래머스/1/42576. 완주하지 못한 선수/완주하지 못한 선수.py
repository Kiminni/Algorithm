def solution(participant, completion):
    dic = {}
    for p in participant:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    
    for c in completion:
        if c in dic:
            dic[c] -= 1
    
    for d in dic:
        if dic[d] == 1:
            return d