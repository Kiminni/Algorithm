def solution(myString, pat):
    answer = 0
    tmp = []
    tmp_pat = []
    for i in range(len(myString)):
        if myString[i] == 'A':
            tmp.append('B')
        else:
            tmp.append('A')
    myString= ''.join(tmp)
    
    if pat in myString:
        return 1
    
    
    return 0