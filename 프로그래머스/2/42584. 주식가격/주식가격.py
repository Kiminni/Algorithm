from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        p = prices.popleft()
        tmp = 0
        for price in prices:
            tmp += 1    
            if p > price:
                break
        
        answer.append(tmp)
    
    return answer