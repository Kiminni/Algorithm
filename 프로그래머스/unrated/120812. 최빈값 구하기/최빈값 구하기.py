def solution(array):
    set_array = set(array)
    answer = 0
    max_count = 0
    
    for i in set_array:
        
        count = array.count(i)
        
        if count > max_count:
            max_count = count
            answer = i
        
        elif max_count == count:
            answer = -1
    
    return answer
