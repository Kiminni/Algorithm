from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while prices :
        price = prices.popleft()
        time = 0
        for p in prices:
            time += 1
            if price > p:
                break
        answer.append(time)
        
    return answer

    prices = deque(prices)
    answer = []
    while prices:
        price = prices.popleft()
        time = 0
        for p in prices:
            if price >= p :
                time += 1
            else:
                break
        answer.append(time)