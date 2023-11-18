def solution(my_string):
    
    answer = 0
    tmp = 0
    
    string_list = list(my_string)
    check = ["1","2","3","4","5","6","7","8","9", "0"]
    
    for string in string_list:
        if string in check :
            if tmp > 0 :
                tmp *= 10
            tmp += int(string)
            
        if string not in check:
            answer += tmp
            tmp = 0
    
    answer += tmp
    return answer