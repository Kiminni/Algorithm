def solution(my_string):
    string_list = list(my_string)
    answer = ''
    for tmp in string_list:
        if tmp not in ['a','e','i','o','u'] :
            answer += tmp
    return answer
        
    