def solution(names):
    temp = []
    result = []
    for i in range(len(names)):
        temp.append(names[i])
        if (i + 1) % 5 == 0:
            result.append(temp[0])
            temp = []
    
    if len(temp) != 0:
        result.append(temp[0])
            
    return result