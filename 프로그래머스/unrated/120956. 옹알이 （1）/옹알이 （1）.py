def solution(babbling):
    answer = 0
    bab_list = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        tmp = ''
        for j in range(len(babbling[i])):
            tmp += babbling[i][j]
            
            if tmp == 'aya' :
                tmp = ''
            elif tmp == "ye" :
                tmp = ''
            elif tmp == "woo" :
                tmp = ''
            elif tmp == "ma" :
                tmp = ''
            else:
                continue
            
        if tmp == '':
            answer += 1
            
    return answer