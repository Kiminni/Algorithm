def solution(my_string, is_suffix):
    answer = 0
    ans_list = []
    for i in range(len(my_string)):
        ans_list.append(my_string)
        my_string = my_string[1:]
    
    
    if is_suffix in ans_list:
        return 1
    
    return 0