def solution(numlist, n):
    answer = []
    
    tmp = []
    
    for i in numlist:
        tmp.append([i,abs(n - i)])
    
    tmp.sort(key=lambda x:x[1])
    
    for j in range(len(tmp)):
        answer.append(tmp[j][0])
    
    for k in range(len(answer) - 1): 
        if abs(n - answer[k]) == abs(n - answer[k+1]) :
            if answer[k] < answer[k+1]:
                answer[k+1], answer[k] = answer[k],answer[k+1]
    return answer