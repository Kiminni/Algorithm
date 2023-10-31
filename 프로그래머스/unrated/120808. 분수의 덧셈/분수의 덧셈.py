def solution(numer1, denom1, numer2, denom2):
    answer = []
    ans1 = [numer1, denom1] 
    ans2 = [numer2, denom2]
    
    if denom1 != denom2 :
        denom = denom1 * denom2
        
        numer1 = numer1 * (denom / denom1)
        numer2 = numer2 * (denom / denom2)
        
        answer = [numer1 + numer2, denom]
        tmp = 0
        for i in range(1, 1000):
            if (answer[0] % i) == 0 and (answer[1] % i) == 0:
                tmp = i
        answer[0] /=  tmp
        answer[1] /=  tmp
                
        return answer
    else:
        answer = [numer1 + numer2, denom1]
        tmp = 0
        for i in range(1, 1000):
                if (answer[0] % i) == 0 and (answer[1] % i) == 0:
                    tmp = i

        answer[0] /=  tmp
        answer[1] /=  tmp
    
        return answer