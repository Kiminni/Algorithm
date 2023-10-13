def solution(myString):
    answer = []
    myString = myString.split("x")
    for n in myString:
        answer.append(len(n))
    return answer