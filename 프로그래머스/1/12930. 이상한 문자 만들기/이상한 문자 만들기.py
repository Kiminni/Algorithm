def solution(s):
    s = s.split(" ")
    answer = []
    for str in s:
        tmp = []
        for i in range(len(str)):
            if i % 2 == 0 :
                tmp.append(str[i].upper())
            else:
                tmp.append(str[i].lower())     
        answer.append(''.join(tmp))
    return ' '.join(answer)