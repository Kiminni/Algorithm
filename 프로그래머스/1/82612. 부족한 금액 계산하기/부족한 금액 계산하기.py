def solution(price, money, count):
    summation = 0
    for i in range(1, count + 1):
        summation += price * i
    if money - summation > 0 :
        return 0
    return summation - money