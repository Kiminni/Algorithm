def solution(num_list, n):
    answer = []
    idx = 0
    for i in range(len(num_list)):
        if idx % n == 0:
            answer.append(num_list[i])
            idx = 0
        idx += 1
    return answer