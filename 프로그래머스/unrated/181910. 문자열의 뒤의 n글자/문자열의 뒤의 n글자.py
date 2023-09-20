def solution(my_string, n):
    answer = ''
    i = len(my_string) - n
    while i <= len(my_string) - 1:
        answer += my_string[i]
        i += 1
    return answer