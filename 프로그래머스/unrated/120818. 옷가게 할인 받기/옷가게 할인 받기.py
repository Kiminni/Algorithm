def solution(price):
    if price >= 100000:
        if price >= 300000:
            if price >= 500000:
                return price * 0.8 // 1
            return price * 0.9 // 1
        return price * 0.95 // 1
    return price // 1