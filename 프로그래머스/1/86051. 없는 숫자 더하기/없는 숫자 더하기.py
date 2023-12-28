def solution(numbers):
    num_list = [1,2,3,4,5,6,7,8,9,0]
    tmp_list = []
    
    for i in numbers:
        if i in num_list:
            tmp_list.append(i)
        
    return sum(num_list) - sum(tmp_list)