from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices: 
        count = 0
        price = prices.popleft() 
        for p in prices:
            count += 1
            if price > p :
                break
        answer.append(count)
    return answer