def solution(array):
    answer = 0
    for num in array:
        num_list = list(str(num))
        for i in num_list:
            if i == '7':
                answer += 1
    return answer