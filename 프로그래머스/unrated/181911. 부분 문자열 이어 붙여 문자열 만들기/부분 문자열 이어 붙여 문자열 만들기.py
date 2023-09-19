def solution(my_strings, parts):
    answer = ''
    j = 0
    for string in my_strings:
        for i in range(parts[j][0], parts[j][1] + 1):
            answer += string[i]
        j += 1
    return answer