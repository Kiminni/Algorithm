def solution(my_string, is_prefix):
    answer = 0
    ans_list = []
    
    for i in range(len(my_string)):
        ans_list.append(my_string)
        my_string = my_string[:-1]
    
    for i in range(len(my_string)):
        ans_list.append()
    
    if is_prefix in ans_list:
        return 1
    return 0