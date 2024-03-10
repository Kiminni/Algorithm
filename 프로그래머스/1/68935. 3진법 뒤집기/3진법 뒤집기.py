def solution(n):
    answer = 0
    tmp = []    
    while n > 0 :
        tmp.append(n % 3)
        n = n // 3
    tmp = tmp[::-1]
    for i in range(len(tmp)):
        answer += tmp[i] * (3**i)
    return answer
        
    