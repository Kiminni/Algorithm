def solution(number):
    answer = 0
    str_num = str(number)
    for i in range(len(str_num)):
        answer += int(str_num[i])
    
    if answer >= 9 :
        answer = answer % 9

    return answer