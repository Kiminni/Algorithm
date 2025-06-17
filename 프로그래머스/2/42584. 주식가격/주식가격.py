from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        tmp = 0
        p = prices.popleft()
        for price in prices:
            tmp += 1
            if p > price:
                break
        answer.append(tmp)
    
            
                
        
    return answer