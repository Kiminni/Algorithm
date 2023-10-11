def solution(myString, pat):
    
    list_idx = []
    answer = ''
    idx = myString.find(pat)
    for i in range(0,idx + len(pat)):
        answer += myString[i]
    
    max_idx = 0
    if len(pat) == 1:
        for i in enumerate(myString):
            if i[1] == pat:
                list_idx.append(int(i[0]))
        return myString[:list_idx[-1]+1]
    #idx = max(list_idx)
            
    return answer