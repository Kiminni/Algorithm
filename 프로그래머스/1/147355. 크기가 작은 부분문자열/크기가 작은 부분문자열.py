def solution(t, p):
    answer = 0
    tl = len(t)
    pl = len(p)
    ip = int(p)
    for i in range(tl - pl + 1):
        now = int(t[i:i+pl])

        if now <= ip:
            answer += 1

    return answer
    
        
    
    return answer