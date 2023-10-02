
def solution(my_string, indices):
    answer = ''
    list_str = []
    for i in range(len(my_string)):
        list_str.append(my_string[i])
    
    list_idx = 0
    indices = sorted(indices)

    for idx in range(len(list_str)):
        if idx == indices[list_idx]:
            list_str[idx] = ''
            list_idx += 1
            
            if list_idx == len(indices):
                break
    return ''.join(list_str)