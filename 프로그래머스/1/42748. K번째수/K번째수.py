def solution(array, commands):
    answer = []
    for com in commands:
        tmp = [] 
        tmp.append(sorted(array[com[0] - 1 :com[1]]))   
        answer.append(tmp[0][com[2] - 1])
        

    return answer