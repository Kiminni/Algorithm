def solution(name, yearning, photo):
    dictionary = dict(zip(name, yearning))
    answer = []
    for pho in photo:
        tmp = 0
        for name in pho:
            if dictionary.get(name) == None:
                continue
            tmp += dictionary.get(name)
        answer.append(tmp)
    
    return answer