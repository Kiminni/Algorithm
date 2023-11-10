def solution(my_string):
    tmp = ''
    for string in my_string:
        if string not in tmp:
            tmp += string
    return tmp