def solution(strArr):
    answer = 0
    count_list = [0]*31
    
    for i in range(len(strArr)):
        count_list[len(strArr[i])] += 1
  
    return max(count_list)