def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:
            answer[stack[-1][0]] = i - stack[-1][0]
            stack.pop()
        stack.append((i, prices[i]))
    
    while stack:
        answer[stack[-1][0]] = (len(prices) - 1) - stack[-1][0]
        stack.pop()
    return answer
        
    