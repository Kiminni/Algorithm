from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    needed = sum(number)
    
    for i in range(len(number)):
        dic[want[i]] = number[i]
    dic = Counter(dic)
    
    tmp = 0
    while tmp + needed <= len(discount):
        discount_counter = Counter(discount[tmp:tmp + needed])
        if discount_counter == dic:
            answer += 1
        tmp += 1

    return answer