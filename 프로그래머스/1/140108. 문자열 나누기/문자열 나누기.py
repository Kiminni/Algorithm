def solution(s):
    answer = 0
    s_list = list(s)
    x = ''
    nx = ''
    for i in s_list:
        if x == '' or x[0] == i:
            x += i
        elif x[0] != i :
            nx += i
            
        if len(x) == len(nx):
            answer += 1
            x = ''
            nx = ''
        
    if x != '':
        answer += 1
    
    return answer