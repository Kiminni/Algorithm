def solution(arr):
    answer = []
    
    start = 0
    end = 0
    flag = 0
    
    for i in range(len(arr)):
        if arr[0] == 2: 
            flag = 1
            break
        if arr[i] == 2 and start == 0:
            start = i

        elif arr[i] == 2 and start != 0: 
            end = i
    
    if flag == 1:
        for j in range(len(arr) - 1):
            if arr[j+1] == 2:
                end = j+1
            
    if start < end:
        for idx in range(start, end + 1):
            answer.append(arr[idx])
    
    
    if start > end:
        return [2]
    
    if answer == []:
        return [-1]
    
    return answer