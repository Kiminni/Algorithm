def solution(array, n):
    answer = []
    array.sort()
    for num in array:
        tmp = abs(n - num)
        answer.append(tmp)

    idx = answer.index(min(answer))
    
    return array[idx]