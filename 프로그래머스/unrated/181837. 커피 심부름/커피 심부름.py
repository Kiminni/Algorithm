def solution(order):
    answer = 0
    for val in order:
        if 'cafelatte' in val:
            answer += 5000
        elif 'americano' in val:
            answer += 4500
        elif val == 'anything':
            answer += 4500
            
    return answer