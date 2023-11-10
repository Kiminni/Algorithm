def solution(s):
    answer = 0
    s_list = s.split(" ")
    for idx in range(len(s_list)):
        if s_list[idx] == 'Z':
            answer -= int(s_list[idx - 1])
            continue
        answer += int(s_list[idx])
        
    return answer
