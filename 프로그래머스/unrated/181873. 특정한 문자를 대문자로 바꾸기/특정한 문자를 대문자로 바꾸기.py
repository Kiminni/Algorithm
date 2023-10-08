def solution(myString, alp):
    answer = ''

    for i in myString:
        if i == alp :
            i = i.upper()
        else:
            i = i.lower()

        answer += i

    return answer