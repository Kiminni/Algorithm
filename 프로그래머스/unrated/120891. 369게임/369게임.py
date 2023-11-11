def solution(order):
    answer = 0
    order_list = list(str(order))
    for ord in order_list:
        if ord == '3' or ord == '6' or ord == '9':
            answer += 1
    return answer