"""
원래 가격 price원
N번째 이용하면 price 가격의 N배를 받습니다.
1번째 100 / 2번째 200 / 3번째 300
count번 탈 때, 얼마가 모자라는지를 반환합니다.
단, 금액이 부족하지 않다면 0을 반환합니다.

money = 내가 갖고 있는 돈
1번 money - price *  
2번 money - price * 1 - price * 2
3번 money - price * 1 - price * 2 - price * 3

n 번 money - price * 1 - price *2 ... price * n
"""
def solution(price, money, count):
    temp = 0
    for i in range(1, count + 1): # 3 6 9 12
        money = money - price * i # 20 - 3 - 6 -9 - 12
        print(money)
    if money > 0:
        return 0
    return abs(money)
    