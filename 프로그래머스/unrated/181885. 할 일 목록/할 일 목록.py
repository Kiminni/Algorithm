def solution(todo_list, finished):
    answer = []
    idx = 0
    for finish in finished:
        if finish == False:
            answer.append(todo_list[idx])
        idx += 1
    return answer