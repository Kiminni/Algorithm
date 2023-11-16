def solution(my_str, n):
    answer = []
    my_list = list(my_str)
    tmp = ''
    for i in my_list:
        tmp += i
        if len(tmp) == n:
            answer.append(tmp)
            tmp = ''
    if tmp != '':
        answer.append(tmp)
    
    return answer