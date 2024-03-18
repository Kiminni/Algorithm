def solution(food):
    answer = ''
    tmp = []
    for i in range(len(food)):
        for j in range(food[i] // 2):
            tmp.append(str(i))

    return ''.join(tmp) + '0' + ''.join(reversed(tmp))