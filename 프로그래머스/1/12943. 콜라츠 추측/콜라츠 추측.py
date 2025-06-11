def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            return answer
        if num % 2 == 0:
            num = num // 2
            answer += 1
        elif num % 2 == 1:
            num = num * 3 + 1
            answer += 1
        
    return -1
