def solution(myStr):
    tmp = []
    answer = []
    string = ''
    for i in range(len(myStr)):
        if myStr[i] == 'a' or myStr[i] == 'b' or myStr[i] == 'c':
            i += 1
            tmp.append(string)
            string = ''
            continue
        string += myStr[i]
    tmp.append(string)
    
    print(answer)
        
    for i in tmp:
        if i != "":
            answer.append(i)
            
    if answer == []:
        return ["EMPTY"]
    return answer