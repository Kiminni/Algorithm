def solution(dartResult):
    tmp = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
            tmp += i
        
        elif i == 'S':
            score.append(int(tmp) ** 1)
            tmp = ''
        
        elif i == 'D':
            score.append(int(tmp) ** 2)
            tmp = ''
        
        elif i == 'T':
            score.append(int(tmp) ** 3)
            tmp = ''
        
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
            
        elif i == '#':
            score[-1] *= -1
            
    return sum(score)