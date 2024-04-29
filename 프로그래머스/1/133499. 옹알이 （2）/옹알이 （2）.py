def solution(babbling):
    babbling_list = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for bab in babbling:
        tmp = []
        before = ''    
        for i in range(len(bab)):
            tmp.append(bab[i])
            print(tmp, before)
            if ''.join(tmp) in babbling_list:
                if before == '':
                    before = ''.join(tmp)
                    tmp = []    
                elif before == ''.join(tmp):
                    break
                else:
                    before = ''.join(tmp)
                    tmp = []
            
        if tmp == []:
            answer += 1
        
    return answer