def solution(my_string):
    answer = 0  
    for i in range(len(my_string)):
        if my_string[i] >= '0' and my_string[i] <= '9':
            answer += int(my_string[i])
    return answer