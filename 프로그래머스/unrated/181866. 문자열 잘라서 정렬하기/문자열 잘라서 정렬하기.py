def solution(myString):
    answer = []
    tmp = myString.split("x")
    for i in tmp:
        if i != "":
            answer.append(i)
        
    
    answer.sort()
    return answer