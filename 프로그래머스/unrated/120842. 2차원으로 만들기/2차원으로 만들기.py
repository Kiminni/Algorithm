def solution(num_list, n):
    answer = []
    
    tmp = []
    for i in range(len(num_list)):
        
        tmp.append(num_list[i])
        if len(tmp) == n:
            answer.append(tmp)
            tmp = []
        
    return answer