def solution(myString):
    answer = [x.lower() for x in myString]
    for i in range(len(answer)):
        if answer[i] == 'a' :
            answer[i] = 'A'
    return ''.join(answer)