def solution(q, r, code):
    answer = ''
    temp = []
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
                
    return answer