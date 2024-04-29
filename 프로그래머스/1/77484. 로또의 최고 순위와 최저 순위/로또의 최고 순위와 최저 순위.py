def solution(lottos, win_nums):
    ans_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    min_answer = 0
    max_answer = 0
    for i in lottos:
        if i in win_nums:
            min_answer += 1
            max_answer += 1
        elif i == 0 :
            max_answer += 1
    
    return [ans_dict[max_answer], ans_dict[min_answer]]