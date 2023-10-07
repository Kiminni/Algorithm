def solution(num_list, n):
    answer = []
    i = 0
    for num in num_list:
        if i < n:
            answer.append(num)
        i += 1
    return answer