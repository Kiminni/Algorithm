def solution(my_string):
    tmp = []
    for i in range(len(my_string)):
        if my_string[i] >= '0' and my_string[i] <= '9':
            tmp.append(int(my_string[i]))
    tmp.sort()
    
    return tmp