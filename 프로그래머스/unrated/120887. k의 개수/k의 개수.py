def solution(i, j, k):
    num_list = []
    answer = 0
    for num in range(i, j + 1):
        num_list.append(str(num))
    
    for n in num_list:
        for str_n in n:
            if str_n == str(k):
                answer += 1
    return answer