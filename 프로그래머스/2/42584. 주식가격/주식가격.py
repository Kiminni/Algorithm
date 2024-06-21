from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        price = prices.popleft()
        count = 0
        for p in prices:
            count += 1
            if p < price:
                break
        answer.append(count)
    return answer