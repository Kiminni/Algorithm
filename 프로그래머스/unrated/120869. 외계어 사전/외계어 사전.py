def solution(spell, dic):
    
    for dict in dic:
        cnt = 0
        for s in spell:
            if s in dict:
                cnt += 1
        if len(spell) == cnt:
            return 1
        
    return 2