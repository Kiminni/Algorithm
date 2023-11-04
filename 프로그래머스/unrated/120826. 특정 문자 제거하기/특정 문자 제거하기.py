def solution(my_string, letter):
    tmp = ''
    for i in range(len(my_string)):
        if my_string[i] == letter:
            continue
        tmp += my_string[i]
    return tmp