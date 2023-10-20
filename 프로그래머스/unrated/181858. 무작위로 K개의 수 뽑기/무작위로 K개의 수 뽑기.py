def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    
    if len(answer) > k:
        answer = answer[:k]
    
    else: 
        answer.extend([-1] * (k - len(answer)))
    return answer