def solution(n):
    answer = []
    for i in range(2, n+1):
        if n % i == 0:
            answer.append(i)
            answer.append(n // i)
    
    answer = list(set(answer))
    answer.sort()
    if n == 1:
        return [1]
    return answer