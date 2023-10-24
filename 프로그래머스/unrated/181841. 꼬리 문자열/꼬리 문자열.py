def solution(str_list, ex):
    tmp = []
    for i in str_list:
        if ex not in i:
            tmp.append(i)
    return ''.join(tmp)