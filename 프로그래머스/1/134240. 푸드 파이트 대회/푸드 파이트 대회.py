def solution(food):
    answer = ''
    tmp = []
    for i in range(len(food)):
        for j in range(food[i] // 2):
            tmp.append(str(i))
    tmp_rev = reversed(tmp)
    tmp.append('0')
    
    return ''.join(tmp) + ''.join(tmp_rev)