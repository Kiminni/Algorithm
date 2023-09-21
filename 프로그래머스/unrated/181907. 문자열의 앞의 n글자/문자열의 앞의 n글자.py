def solution(my_string, n):
    answer = ''
    ans_list = []
    for i in range(n):
        ans_list.append(my_string[i])
    return ''.join(ans_list)