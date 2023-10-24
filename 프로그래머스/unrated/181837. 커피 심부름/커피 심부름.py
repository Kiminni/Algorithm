def solution(order):
    answer = 0
    for val in order:
        if 'cafelatte' in val:
            answer += 5000
        else:
            answer += 4500
            
    return answer