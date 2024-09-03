def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(answer)):
        for j in range(i + 1, len(answer)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
                 
        
    