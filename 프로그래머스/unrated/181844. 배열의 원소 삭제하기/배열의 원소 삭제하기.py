def solution(arr, delete_list):
    answer = []
    for idx in arr:
        if idx not in delete_list:
            answer.append(idx)
    
    return answer